"""Numerical and command-line contracts for the bundled contrast checker."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "ui-design-principles" / "scripts" / "check_contrast.py"
SPEC = importlib.util.spec_from_file_location("check_contrast", SCRIPT)
contrast = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(contrast)


def run_check(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args], capture_output=True, text=True, check=False
    )


class ContrastTests(unittest.TestCase):
    def test_black_white_and_equal_colors(self):
        self.assertEqual(contrast.contrast_ratio("#000", "#fff"), 21)
        self.assertEqual(contrast.contrast_ratio("#1976D2", "#1976d2"), 1)

    def test_shorthand_and_case_normalize(self):
        self.assertEqual(contrast.normalize_hex("#aB3"), "#AABB33")
        self.assertEqual(contrast.normalize_hex("#abcdef"), "#ABCDEF")

    def test_ratio_is_symmetric(self):
        self.assertEqual(
            contrast.contrast_ratio("#123456", "#fedcba"),
            contrast.contrast_ratio("#fedcba", "#123456"),
        )

    def test_srgb_piecewise_boundary(self):
        self.assertEqual(contrast.linearize_srgb(0.04045), 0.04045 / 12.92)
        just_below = 0.04045 - 1e-8
        just_above = 0.04045 + 1e-8
        self.assertEqual(contrast.linearize_srgb(just_below), just_below / 12.92)
        self.assertAlmostEqual(
            contrast.linearize_srgb(just_above), ((just_above + 0.055) / 1.055) ** 2.4
        )

    def test_eight_bit_values_around_breakpoint(self):
        self.assertAlmostEqual(contrast.relative_luminance("#0a0a0a"), (10 / 255) / 12.92)
        self.assertAlmostEqual(
            contrast.relative_luminance("#0b0b0b"), ((11 / 255 + 0.055) / 1.055) ** 2.4
        )

    def test_known_gray_ratio(self):
        self.assertAlmostEqual(contrast.contrast_ratio("#777", "#fff"), 4.478089453577214, places=12)

    def test_rejects_unsupported_color_inputs(self):
        for value in ("fff", "#12", "#1234", "#12345678", "#ggg", "red", "transparent", "rgb(0 0 0)", "var(--text)", " #fff", "#fff\n"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                contrast.normalize_hex(value)

    def test_cli_json_and_exit_contract(self):
        passed = run_check("#000", "#fff", "--json", "--minimum", "21")
        self.assertEqual(passed.returncode, 0)
        self.assertEqual(json.loads(passed.stdout), {
            "foreground": "#000000", "background": "#FFFFFF", "ratio": 21.0,
            "minimum": 21.0, "passes": True,
        })
        failed = run_check("#777", "#fff", "--json")
        self.assertEqual(failed.returncode, 1)
        self.assertFalse(json.loads(failed.stdout)["passes"])

    def test_threshold_is_inclusive_and_unrounded(self):
        ratio = contrast.contrast_ratio("#777", "#fff")
        equal = run_check("#777", "#fff", "--minimum", repr(ratio), "--json")
        rounded_up = run_check("#777", "#fff", "--minimum", "4.48", "--json")
        self.assertEqual(equal.returncode, 0)
        self.assertEqual(rounded_up.returncode, 1)
        self.assertLess(json.loads(rounded_up.stdout)["ratio"], 4.48)

    def test_minimum_one_accepts_equal_colors(self):
        self.assertEqual(run_check("#fff", "#fff", "--minimum", "1").returncode, 0)

    def test_cli_rejects_invalid_thresholds_and_colors(self):
        for minimum in ("0", "0.99", "21.01", "-1", "nan", "inf", "-inf", "potato"):
            with self.subTest(minimum=minimum):
                result = run_check("#000", "#fff", "--minimum=" + minimum)
                self.assertEqual(result.returncode, 2)
                self.assertIn("minimum", result.stderr)
        result = run_check("#0008", "#fff")
        self.assertEqual(result.returncode, 2)
        self.assertIn("opaque sRGB", result.stderr)


if __name__ == "__main__":
    unittest.main()
