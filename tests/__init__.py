from pathlib import Path

def load_tests(loader, tests, pattern):
    root = Path(__file__).resolve().parent
    return loader.discover(
        start_dir=str(root),
        pattern="test_*.py",
        top_level_dir=str(root.parent),
    )
