import os
from pathlib import Path

_base_dir = os.path.abspath(os.path.dirname(__file__))
_base_dir_pathlib = Path(_base_dir)
_resources_dir_pathlib = _base_dir_pathlib / "resources"
_stored_mouse_positions_dir_pathlib = _resources_dir_pathlib / "stored_mouse_positions"
_chromedriver_pathlib = _resources_dir_pathlib / "chromedriver"


def create_valid_file_path(target_file_path):
    file_path = target_file_path
    i = 1
    while file_path.exists():
        file_path = Path(
            file_path.parent, f"{target_file_path.stem}_{i}{file_path.suffix}",
        )
        i += 1

    return file_path


def prRed(skk):
    print("\033[91m{}\033[00m".format(skk))


def prGreen(skk):
    print("\033[92m{}\033[00m".format(skk))
