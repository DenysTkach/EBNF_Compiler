#!/usr/bin/env python3
"""Test all example files"""
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.frontend import parse_source, load_source
from src.sema import SemanticAnalyzer, SemanticError

def test_file(filepath):
    """Test a single file"""
    filename = os.path.basename(filepath)
    try:
        code = load_source(filepath)
        ast = parse_source(code)
        analyzer = SemanticAnalyzer()
        analyzer.analyze(ast)
        return True, "OK"
    except SemanticError as e:
        return False, f"SEMANTIC ERROR: {e}"
    except Exception as e:
        return False, f"ERROR: {e}"

def main():
    examples_dir = Path("examples")
    files = sorted(examples_dir.glob("*.mod"))

    print(f"Testing {len(files)} example files...\n")

    passed = 0
    failed = 0

    for filepath in files:
        success, message = test_file(filepath)
        status = "[OK]" if success else "[FAIL]"

        if success:
            print(f"{status} {filepath.name:40s} {message}")
            passed += 1
        else:
            print(f"{status} {filepath.name:40s} {message}")
            failed += 1

    print(f"\n{'='*70}")
    print(f"Total: {len(files)} | Passed: {passed} | Failed: {failed}")

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
