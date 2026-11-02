#!/usr/bin/env python3
"""Validate this repository's authored skill format using only Python's stdlib.

This intentionally checks a small, documented authoring convention rather than
implementing general YAML or Markdown. Frontmatter has exactly an unquoted name
and a JSON-compatible double-quoted single-line description. Local links use
ordinary Markdown inline-link syntax, without optional link titles.
"""

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SKILL = REPOSITORY_ROOT / "skills" / "sajid-ui-design"
LINK = re.compile(r"!?\[[^\]\n]*\]\(\s*([^\n)]*?)\s*\)")
HEADING = re.compile(r"^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def prose_lines(text):
    """Yield non-fenced lines, preserving their original line numbers."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if match:
            mark = match.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield number, line


def heading_anchors(text):
    """Support normal GitHub-style heading slugs, including repeated headings."""
    anchors = set()
    used = set()
    for _, line in prose_lines(text):
        match = HEADING.match(line)
        if match is None:
            continue
        title = match.group(2)
        title = LINK.sub(lambda link: link.group(0).split("]", 1)[0].lstrip("!["), title)
        title = re.sub(r"<[^>]*>", "", title).lower()
        slug = "".join(
            char for char in title
            if char in "-_ " or unicodedata.category(char)[0] in "LN"
        ).replace(" ", "-")
        candidate = slug
        suffix = 1
        while candidate in used:
            candidate = f"{slug}-{suffix}"
            suffix += 1
        used.add(candidate)
        anchors.add(candidate)
    # Explicit HTML anchors are common in Markdown source inventories.
    anchors.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    return anchors


def markdown_links(text):
    for number, line in prose_lines(text):
        for match in LINK.finditer(line):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            yield number, line, target


def is_inside(path, root):
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def local_target(document, target, root):
    """Return (resolved path, fragment), or None for an external URL."""
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    decoded_path = unquote(parsed.path)
    if decoded_path.startswith("/") or "\\" in decoded_path:
        raise ValueError("local links must use relative POSIX paths")
    resolved = (document.parent / decoded_path).resolve() if decoded_path else document.resolve()
    if not is_inside(resolved, root):
        raise ValueError("local link escapes the portable skill directory")
    if parsed.query:
        raise ValueError("local links must not include query strings")
    return resolved, unquote(parsed.fragment)


def bundled_files(directory):
    if not directory.is_dir():
        return []
    return sorted(
        path for path in directory.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
        and not any(part.startswith(".") for part in path.relative_to(directory).parts)
    )


def reference_map_range(text):
    start = None
    depth = None
    end = len(text.splitlines()) + 1
    for number, line in prose_lines(text):
        match = HEADING.match(line)
        if match is None:
            continue
        if start is None:
            if len(match.group(1)) <= 2 and match.group(2).lower() == "reference map":
                start, depth = number, len(match.group(1))
        elif len(match.group(1)) <= depth:
            end = number
            break
    return None if start is None else (start, end)


def validate_skill(directory):
    """Return a list of human-readable errors; do not mutate any files."""
    root = Path(directory).resolve()
    skill = root / "SKILL.md"
    errors = []
    if not skill.is_file():
        return [f"{skill}: missing SKILL.md"]
    text = skill.read_text(encoding="utf-8")
    lines = text.splitlines()

    def report(path, message, line=None):
        label = str(path.relative_to(root)) if is_inside(path, root) else str(path)
        errors.append(f"{label}{':' + str(line) if line else ''}: {message}")

    if len(lines) >= 500:
        report(skill, f"{len(lines)} lines; SKILL.md must contain fewer than 500")
    closing = lines.index("---", 1) if lines and "---" in lines[1:] else None
    if not lines or lines[0] != "---" or closing is None:
        report(skill, "missing YAML frontmatter delimiters")
    else:
        fields = {}
        for number in range(1, closing):
            line = lines[number]
            if not line.strip():
                continue
            match = re.fullmatch(r"([a-z-]+): (.+)", line)
            if match is None:
                report(skill, "use single-line 'name: value' and 'description: \"...\"' fields", number + 1)
                continue
            key, value = match.groups()
            if key in fields:
                report(skill, f"duplicate frontmatter field {key}", number + 1)
            fields[key] = value
        if set(fields) != {"name", "description"}:
            report(skill, "authored frontmatter must contain exactly name and description")
        name = fields.get("name", "")
        if not 1 <= len(name) <= 64 or NAME.fullmatch(name) is None:
            report(skill, "name must be 1–64 lowercase letters/digits/single hyphens")
        if name != root.name:
            report(skill, f"name {name!r} must match directory {root.name!r}")
        try:
            description = json.loads(fields.get("description", ""))
        except json.JSONDecodeError:
            description = None
        if not isinstance(description, str) or not description.strip() or not 1 <= len(description) <= 1024:
            report(skill, "description must be a JSON-compatible double-quoted string of 1–1024 characters")

    routing = reference_map_range(text)
    if routing is None:
        report(skill, "missing '# Reference map' or '## Reference map' section")
    linked_from_skill = set()
    routed_references = set()
    documents = [skill] + [path for path in bundled_files(root) if path.suffix == ".md" and path != skill]
    for document in documents:
        content = text if document == skill else document.read_text(encoding="utf-8")
        if "references" in document.relative_to(root).parts and len(content.splitlines()) > 100:
            has_contents = any(
                HEADING.match(line) and HEADING.match(line).group(2).lower() == "contents"
                for _, line in prose_lines(content)
            )
            if not has_contents:
                report(document, "references longer than 100 lines require a Contents heading")
        for number, line, target in markdown_links(content):
            if not target:
                report(document, "empty Markdown link target", number)
                continue
            try:
                result = local_target(document, target, root)
            except ValueError as error:
                report(document, f"{target}: {error}", number)
                continue
            if result is None:
                continue
            resolved, fragment = result
            if not resolved.exists():
                report(document, f"local link does not exist (including exact case): {target}", number)
                continue
            if fragment:
                if resolved.suffix != ".md" or not resolved.is_file():
                    report(document, f"cannot resolve Markdown heading fragment: {target}", number)
                elif fragment not in heading_anchors(resolved.read_text(encoding="utf-8")):
                    report(document, f"heading anchor does not exist: {target}", number)
            if document == skill:
                linked_from_skill.add(resolved)
                if routing and routing[0] < number < routing[1] and line.lstrip().startswith("|"):
                    routed_references.add(resolved)

    for reference in bundled_files(root / "references"):
        if reference.resolve() not in routed_references:
            report(reference, "must be directly linked in the SKILL.md Reference map table")
    for folder in ("scripts", "assets"):
        for resource in bundled_files(root / folder):
            if resource.resolve() not in linked_from_skill:
                report(resource, "must be directly linked from SKILL.md")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_directory", nargs="?", type=Path, default=DEFAULT_SKILL)
    args = parser.parse_args(argv)
    try:
        errors = validate_skill(args.skill_directory)
    except (OSError, UnicodeError) as error:
        print(f"ERROR: cannot read skill files: {error}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {args.skill_directory.name} structure, reference routing, and local links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
