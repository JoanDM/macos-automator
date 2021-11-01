from automator_class import Automator

IDLE_START_TIME_SEC = 3


def run_automated_process():
    automator = Automator()

    # START PROGRAM
    print(f"\nStarted automated process!!\n" f"To stop the process use ctrl+C...\n")

    try:
        print(
            f"MacOS Spotlight search will be launched in {IDLE_START_TIME_SEC} seconds..."
        )
        automator.idle_time(3)
        automator.search_spotlight_and_launch("terminal")
        print(
            f"Running echo Hello World on Terminal in {IDLE_START_TIME_SEC} seconds..."
        )
        automator.idle_time(3)
        automator.type("echo Hello World")
        automator.press_enter()

    except KeyboardInterrupt:
        print("\nProcess interrupted sucessfully")


if __name__ == "__main__":
    run_automated_process()
