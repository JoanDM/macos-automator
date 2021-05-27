from automator_class import Automator
from config import _stored_mouse_positions_dir_pathlib

FILE_PATH = _stored_mouse_positions_dir_pathlib / "mouse_positions_example.txt"

IDLE_TIME = 5


def run_infinite_mouse_click():
    automator = Automator()

    print(f"\nStarted automated process!!\n" f"To stop the process use ctrl+C...\n")

    positions_json = automator.get_mouse_positions_from_file(FILE_PATH)

    try:
        for key, position in positions_json.items():

            print(f"Clicking {position} in {IDLE_TIME} seconds...")
            automator.idle_time(IDLE_TIME)
            automator.click(position)

    except KeyboardInterrupt:
        print("\nProcess interrupted sucessfully")


if __name__ == "__main__":
    run_infinite_mouse_click()
