"""Check the explicit opaque color-pair contract of the optional example asset.

This deliberately parses only the starter's simple hex declarations, not CSS in
general. It checks declared pairs, not compositing or rendered accessibility.
"""

import importlib.util
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "sajid-ui-design"
SPEC = importlib.util.spec_from_file_location("palette_contrast", SKILL / "scripts" / "check_contrast.py")
contrast = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(contrast)


class StarterPaletteTests(unittest.TestCase):
    def test_declared_color_pairs_in_both_themes(self):
        css = (SKILL / "assets" / "token-starter.css").read_text(encoding="utf-8")
        for theme in ("light", "dark"):
            block = re.search(r'\[data-theme="' + theme + r'"\]\s*\{(.*?)\}', css, re.S)
            self.assertIsNotNone(block, f"missing explicit {theme} theme")
            tokens = dict(re.findall(r"--ui-([a-z-]+):\s*(#[0-9a-fA-F]{6});", block.group(1)))
            pairs = []
            for background in ("canvas", "surface", "surface-raised", "surface-recessed"):
                pairs.extend((foreground, background, 4.5) for foreground in
                             ("text", "text-muted", "danger", "warning", "success", "info"))
                pairs.extend((foreground, background, 3) for foreground in ("border", "focus"))
            pairs.extend(("on-action", background, 4.5) for background in
                         ("action", "action-hover", "action-pressed"))
            pairs.append(("on-selection", "selection", 4.5))
            for foreground, background, minimum in pairs:
                with self.subTest(theme=theme, foreground=foreground, background=background):
                    self.assertIn(foreground, tokens)
                    self.assertIn(background, tokens)
                    self.assertGreaterEqual(contrast.contrast_ratio(tokens[foreground], tokens[background]), minimum)


if __name__ == "__main__":
    unittest.main()
