import os
from pathlib import Path

_base_dir = os.path.abspath(os.path.dirname(__file__))
_base_dir_pathlib = Path(_base_dir)
_resources_dir_pathlib = _base_dir_pathlib / "resources"
_stored_mouse_positions_dir_pathlib = _resources_dir_pathlib / "stored_mouse_positions"


def prRed(skk):
    print("\033[91m{}\033[00m".format(skk))


def prGreen(skk):
    print("\033[92m{}\033[00m".format(skk))
