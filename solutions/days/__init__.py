from importlib import import_module
from pathlib import Path
from re import match


def main():
    for fpath in sorted(Path(__file__).parent.iterdir(), key=lambda p: p.name):
        if match(r"^day\d{2}\.py", fpath.name):
            import_module(f".{fpath.name[:-3]}", package=__name__).main()
