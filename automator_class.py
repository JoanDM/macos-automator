from pynput.mouse import Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button
from pynput.keyboard import Key
from datetime import datetime
import subprocess
import ast


class Automator(object):
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()

    def idle_time(self, timeout_sec):
        previous_time = datetime.now()
        current_time = datetime.now()
        time_diff = (current_time - previous_time).total_seconds()
        while time_diff < timeout_sec:
            current_time = datetime.now()
            time_diff = (current_time - previous_time).total_seconds()

    def click(self, mouse_position, idle_time=0.05):
        self.mouse.position = mouse_position
        self.idle_time(idle_time)
        self.mouse.click(Button.left, 1)
        self.idle_time(idle_time)

    def double_click(self, mouse_position):
        self.mouse.position = mouse_position
        self.idle_time(1)
        self.mouse.click(Button.left, 2)
        self.idle_time(1)

    def triple_click(self, mouse_position):
        self.mouse.position = mouse_position
        self.idle_time(1)
        self.mouse.click(Button.left, 3)
        self.idle_time(1)

    def press_cmd_tab(self, idle_time=0.2):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.tab)
        self.idle_time(idle_time)

    def refresh(self, idle_time=1.5):
        self.keyboard.press(Key.cmd)
        self.keyboard.press("r")
        self.keyboard.release(Key.cmd)
        self.keyboard.release("r")
        self.idle_time(idle_time)

    def search_spotlight_and_launch(self, text):
        with self.keyboard.pressed(Key.cmd):
            self.idle_time(0.5)
            self.keyboard.press(Key.space)
            self.keyboard.release(Key.space)
        self.keyboard.release(Key.cmd)
        self.idle_time(1)
        self.keyboard.type(text)
        self.idle_time(3)
        self.type_enter()
        self.idle_time(3)

    def save_keyboard_shortcut(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.idle_time(1)
        self.keyboard.press("s")
        self.keyboard.release("s")
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.idle_time(4)

    def screenshot_keyboard_shortcut(self, idle_time=4):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.keyboard.press("3")
        self.keyboard.release("3")
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.idle_time(idle_time)

    def take_screenshot_with_coordinates(self, top_x, left_y, width, heigth, filename):
        subprocess.check_output(
            ["screencapture", f"-R{top_x},{left_y},{width},{heigth}", f"{filename}.png"]
        )

    def type(self, text):
        self.keyboard.type(text)
        self.idle_time(0.5)

    def type_enter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        self.idle_time(0.5)

    def get_mouse_positions_from_file(self, file_path):

        positions = open(file_path)
        return ast.literal_eval(positions.readline())
