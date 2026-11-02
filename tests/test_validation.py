"""Prove missing resources and orphan references fail the package checks."""

import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / ".github" / "scripts" / "validate_skill.py"
SPEC = importlib.util.spec_from_file_location("validate_skill", SCRIPT)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


SKILL_TEXT = '''---
name: example-skill
description: "Design and review a frontend interface."
---

# Example skill

Read the routed reference before making that decision.

## Reference map

| Situation | File |
| --- | --- |
| Color work | [Color](references/color.md#contrast) |

## Tools

[Checker](scripts/check.py) and [Tokens](assets/tokens.css).
'''


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.skill = Path(self.temp.name) / "example-skill"
        self.write("SKILL.md", SKILL_TEXT)
        self.write("references/color.md", "# Color\n\n## Contrast\n\nCompare actual rendered colors.\n")
        self.write("scripts/check.py", "print('check')\n")
        self.write("assets/tokens.css", ":root { --text: #111; }\n")

    def write(self, relative, content):
        path = self.skill / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def errors(self):
        return validator.validate_skill(self.skill)

    def test_valid_fixture(self):
        self.assertEqual(self.errors(), [])

    def test_unlisted_reference_fails_even_if_linked_elsewhere(self):
        self.write("references/spacing.md", "# Spacing\n")
        self.write("SKILL.md", SKILL_TEXT + "\nRead [Spacing](references/spacing.md).\n")
        self.assertTrue(any("references/spacing.md" in error and "Reference map table" in error for error in self.errors()))

    def test_missing_link_target_fails(self):
        (self.skill / "references" / "color.md").unlink()
        self.assertTrue(any("local link does not exist" in error and "color.md" in error for error in self.errors()))

    def test_missing_heading_fails(self):
        self.write("references/color.md", "# Color\n\n## Different heading\n")
        self.assertTrue(any("heading anchor does not exist" in error for error in self.errors()))

    def test_unlinked_bundled_asset_fails(self):
        self.write("assets/extra.css", ":root {}\n")
        self.assertTrue(any("assets/extra.css" in error and "directly linked" in error for error in self.errors()))

    def test_path_outside_portable_skill_fails(self):
        outside = self.skill.parent / "outside.md"
        outside.write_text("# Outside\n", encoding="utf-8")
        self.write("SKILL.md", SKILL_TEXT + "\n[Outside](../outside.md)\n")
        self.assertTrue(any("escapes the portable skill directory" in error for error in self.errors()))

    def test_frontmatter_name_and_description_limits(self):
        self.write("SKILL.md", SKILL_TEXT.replace("name: example-skill", "name: Wrong--name"))
        self.assertTrue(any("name must" in error for error in self.errors()))
        self.write("SKILL.md", SKILL_TEXT.replace("Design and review a frontend interface.", "x" * 1025))
        self.assertTrue(any("description must" in error for error in self.errors()))

    def test_long_reference_requires_contents_heading(self):
        self.write("references/color.md", "# Color\n\n## Contrast\n" + "Content.\n" * 101)
        self.assertTrue(any("Contents heading" in error for error in self.errors()))
        self.write("references/color.md", "# Color\n\n## Contents\n\n- [Contrast](#contrast)\n\n## Contrast\n" + "Content.\n" * 101)
        self.assertEqual(self.errors(), [])

    def test_link_mentioned_only_in_fenced_example_does_not_route(self):
        self.write("SKILL.md", SKILL_TEXT.replace(
            "| Color work | [Color](references/color.md#contrast) |",
            "```markdown\n| Color work | [Color](references/color.md#contrast) |\n```",
        ))
        self.assertTrue(any("Reference map table" in error for error in self.errors()))

    def test_duplicate_heading_fragments_resolve(self):
        self.write("references/color.md", "# Color\n\n## Contrast\n\n## Contrast\n\n[Second](#contrast-1)\n")
        self.assertEqual(self.errors(), [])


class RepositoryBrandingTests(unittest.TestCase):
    """Attribution belongs in CREDITS.md, not in agent decision guidance."""

    def test_generic_skill_and_separate_credits(self):
        skill = ROOT / "skills" / "ui-design-principles"
        self.assertTrue((skill / "SKILL.md").is_file())
        self.assertTrue((skill / "CREDITS.md").is_file())
        self.assertFalse((skill / "references" / "sources.md").exists())

        operational = [ROOT / "README.md", ROOT / "evals" / "scenarios.json"]
        operational += [path for path in skill.rglob("*")
                        if path.is_file() and path.name not in ("CREDITS.md", "LICENSE")]
        for path in operational:
            if path.suffix not in (".md", ".py", ".yaml", ".json", ".css"):
                continue
            with self.subTest(path=path.relative_to(ROOT)):
                content = path.read_text(encoding="utf-8")
                self.assertNotRegex(content.lower(), r"sajid|whosajid|iamsajid")


if __name__ == "__main__":
    unittest.main()
