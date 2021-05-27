from automator_class import Automator
from config import _stored_mouse_positions_dir_pathlib
import ast

FILE_PATH = _stored_mouse_positions_dir_pathlib / "mouse_positions_example.txt"

IDLE_TIME = 5


def execute_clicks_from_file():
    automator = Automator()

    print(f"\nStarted automated process!!\n" f"To stop the process use ctrl+C...\n")

    positions = open(FILE_PATH)
    positions_json = ast.literal_eval(positions.readline())

    try:
        for key, position in positions_json.items():

            print(f"Clicking {position} in {IDLE_TIME} seconds...")
            automator.idle_time(IDLE_TIME)
            automator.click(position)

    except KeyboardInterrupt:
        print("\nProcess interrupted sucessfully")


if __name__ == "__main__":
    execute_clicks_from_file()
