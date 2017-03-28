import os
import tempfile
from contextlib import suppress

from pathlib import Path


def temp_dir(name, root=None):
    root = root or tempfile.gettempdir()
    directory = Path(root) / name
    if os.name == 'nt':
        with suppress(FileExistsError):
            directory.mkdir()
    else:
        directory.mkdir(exist_ok=True)
    return directory
