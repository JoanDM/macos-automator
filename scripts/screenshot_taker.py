from automator_class import Automator
from config import _stored_mouse_positions_dir_pathlib

FILE_PATH = _stored_mouse_positions_dir_pathlib / "mouse_positions_example.txt"

IDLE_TIME = 5


def run_infinite_mouse_click():
    automator = Automator()

    print(f"\nStarted automated process!!\n" f"To stop the process use ctrl+C...\n")

    # screenshot_top_left_corner = (129, 187)
    # screenshot_bottom_right_corner = (2049, 1266)

    automator.idle_time(IDLE_TIME)
    try:
        for i in range(90):

            automator.hold_cmd_key()
            automator.press_right_arrow()
            automator.idle_time(2)
            automator.take_screenshot_with_coordinates(
                129, 187, 2049 - 129, 1266 - 187, f"{str(i).zfill(8)}"
            )
            automator.idle_time(1)

    except KeyboardInterrupt:
        print("\nProcess interrupted sucessfully")


if __name__ == "__main__":
    run_infinite_mouse_click()
