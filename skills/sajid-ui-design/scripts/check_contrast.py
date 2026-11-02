#!/usr/bin/env python3
"""Check a pair of opaque sRGB colors without external dependencies."""

import argparse
import json
import math
import re
import sys


HEX_COLOR = re.compile(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})")


def normalize_hex(value):
    """Return #RRGGBB, rejecting alpha, CSS expressions, and non-hex colors."""
    if not isinstance(value, str) or HEX_COLOR.fullmatch(value) is None:
        raise ValueError("use an opaque sRGB color in #RGB or #RRGGBB form")
    digits = value[1:]
    if len(digits) == 3:
        digits = "".join(channel * 2 for channel in digits)
    return "#" + digits.upper()


def linearize_srgb(channel):
    """Linearize one sRGB channel normalized to the interval [0, 1]."""
    if channel <= 0.04045:
        return channel / 12.92
    return ((channel + 0.055) / 1.055) ** 2.4


def relative_luminance(color):
    """Calculate WCAG relative luminance for an opaque hexadecimal sRGB color."""
    normalized = normalize_hex(color)
    red, green, blue = (
        linearize_srgb(int(normalized[index:index + 2], 16) / 255.0)
        for index in (1, 3, 5)
    )
    return 0.2126 * red + 0.7152 * green + 0.0722 * blue


def contrast_ratio(foreground, background):
    """Return an unrounded contrast ratio, independent of color order."""
    first = relative_luminance(foreground)
    second = relative_luminance(background)
    lighter, darker = max(first, second), min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def minimum_argument(value):
    try:
        minimum = float(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError("minimum must be a number from 1 to 21") from error
    if not math.isfinite(minimum) or not 1 <= minimum <= 21:
        raise argparse.ArgumentTypeError("minimum must be a finite number from 1 to 21")
    return minimum


def color_argument(value):
    try:
        return normalize_hex(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError(str(error)) from error


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Check the WCAG contrast ratio of two opaque sRGB hex colors.",
        epilog=(
            "Accepts #RGB and #RRGGBB only; quote colors in a shell. "
            "Alpha colors, gradients, images, CSS expressions, and other color spaces "
            "are not supported. Resolve the actual rendered, composited colors first. "
            "This checks a color pair, not overall WCAG compliance. "
            "Exit status: 0 passes, 1 below minimum, 2 invalid input. "
            "Threshold comparisons use the unrounded ratio."
        ),
    )
    parser.add_argument("foreground", type=color_argument, help="opaque foreground, e.g. '#334155'")
    parser.add_argument("background", type=color_argument, help="opaque background, e.g. '#fff'")
    parser.add_argument("--minimum", type=minimum_argument, default=4.5, help="required ratio from 1 to 21 (default: 4.5)")
    parser.add_argument("--json", action="store_true", help="emit machine-readable results with an unrounded ratio")
    args = parser.parse_args(argv)
    ratio = contrast_ratio(args.foreground, args.background)
    passes = ratio >= args.minimum
    result = {
        "foreground": args.foreground,
        "background": args.background,
        "ratio": ratio,
        "minimum": args.minimum,
        "passes": passes,
    }
    if args.json:
        print(json.dumps(result, allow_nan=False))
    else:
        print(
            f"{'PASS' if passes else 'FAIL'}: {args.foreground} on {args.background} "
            f"has contrast {ratio:.12g}:1; required {args.minimum:g}:1."
        )
    return 0 if passes else 1


if __name__ == "__main__":
    sys.exit(main())
