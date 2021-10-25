from pynput.keyboard import Key, Listener

from automator_class import Automator


def run_form_filler():
    automator = Automator()

    def on_press(key):
        # print('{0} pressed'.format(
        # key))
        check_key(key)

    def on_release(key):
        # print('{0} release'.format(
        # key))
        if key == Key.esc:
            # Stop listener
            return False

    def check_key(key):
        if str(key) == "'a'":
            automator.erase_character()
            automator.type("Type something for me! :)")

    # Collect events until released
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":

    run_form_filler()
