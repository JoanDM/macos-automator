from pynput import mouse

from config import _stored_mouse_positions_dir_pathlib, create_valid_file_path


def record_mouse_path():
    def on_click(x, y, _, pressed):
        if pressed:
            print(f"Position registered: \t({int(x)}, {int(y)})")
            # pos_name = input("Give a name to record this position. To dismiss the position, insert q...\n>")
            pos_name = f"Pos{len(recorded_mouse_positions.keys()) + 1}"
            recorded_mouse_positions[pos_name] = [int(x), int(y)]

    mouse_listener = mouse.Listener(on_click=on_click)

    recorded_mouse_positions = {}

    try:

        mouse_listener.start()

        print(
            f"\n(x,y) mouse positions will be prompted on screen as integers at every click."
            f"To stop the process use ctrl+C...\n"
        )

        while True:
            pass

    except KeyboardInterrupt:
        mouse_listener.stop()

        if recorded_mouse_positions:

            print(f"\nRecorded mouse positions:\n{recorded_mouse_positions}")
            recorded_mouse_positions_filename = str(
                input(
                    f"Give a name to the file which store the positions (extension not needed)."
                    f"To dismiss the file saving, insert q...\n>"
                )
            )

            if recorded_mouse_positions_filename != "q":
                target_file_path = (
                    _stored_mouse_positions_dir_pathlib
                    / f"{recorded_mouse_positions_filename}.txt"
                )
                file_path = create_valid_file_path(target_file_path)
                f = open(file_path, "w")
                f.write(str(recorded_mouse_positions))
                f.close()

                print(f"Mouse positions sucessfully stored at {file_path}")


if __name__ == "__main__":
    record_mouse_path()
