from importlib import import_module
from pathlib import Path
from re import match


def main(days: list[int] = None):
    if days:
        mods = [f".day{str(d).zfill(2)}" for d in days]
    else:
        mods = [
            f".{p.name[:-3]}"
            for p in sorted(Path(__file__).parent.iterdir(), key=lambda p: p.name)
            if match(r"^day\d{2}\.py", p.name)
        ]
    for mod in mods:
        import_module(mod, package=__name__).main()
