from pathlib import Path

import click


class ClickPathLibPath(click.Path):
    def convert(self, *args, **kwargs):
        path = super().convert(*args, **kwargs)
        return Path(path).expanduser().absolute()


