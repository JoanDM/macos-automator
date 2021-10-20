import ast
import subprocess
from datetime import datetime, timedelta

from beepy import beep
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from config import _chromedriver_pathlib


class Automator(object):
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()
        self.driver = None

    def idle_time(self, timeout_sec):
        previous_time = datetime.now()
        current_time = datetime.now()
        time_diff = (current_time - previous_time).total_seconds()
        while time_diff < timeout_sec:
            current_time = datetime.now()
            time_diff = (current_time - previous_time).total_seconds()

    def click(self, mouse_position, idle_time=0.15):
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

    def beep(self, sound=1):
        beep(sound)

    def initialize_browser(self, minimize_css_overhead=False):
        options = webdriver.ChromeOptions()
        if minimize_css_overhead:
            prefs = {
                "profile.default_content_setting_values": {
                    "cookies": 2,
                    "images": 2,
                    # 'javascript': 2,
                    "plugins": 2,
                    "popups": 2,
                    "geolocation": 2,
                    "notifications": 2,
                    "auto_select_certificate": 2,
                    "fullscreen": 2,
                    "mouselock": 2,
                    "mixed_script": 2,
                    "media_stream": 2,
                    "media_stream_mic": 2,
                    "media_stream_camera": 2,
                    "protocol_handlers": 2,
                    "ppapi_broker": 2,
                    "automatic_downloads": 2,
                    "midi_sysex": 2,
                    "push_messaging": 2,
                    "ssl_cert_decisions": 2,
                    "metro_switch_to_desktop": 2,
                    "protected_media_identifier": 2,
                    "app_banner": 2,
                    "site_engagement": 2,
                    "durable_storage": 2,
                }
            }
            options.add_argument("--start-maximized")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_experimental_option("prefs", prefs)

        self.driver = webdriver.Chrome(
            options=options, executable_path=str(_chromedriver_pathlib)
        )

    def launch_website(self, url, idle_time=0):
        self.driver.get(url)
        self.idle_time(idle_time)

    def get_current_website(self):
        return self.driver.current_url

    def select_dropdown_list_xpath(self, xpath, text):
        select = Select(self.driver.find_element_by_xpath(xpath))

        # select by visible text
        select.select_by_visible_text(text)

        # select by value
        # select.select_by_value('1')

    def click_xpath(self, xpath, idle_time_after_click=0.25):
        id_found = False
        while not id_found:
            try:
                self.driver.find_element_by_xpath(xpath).click()
                id_found = True
            except (IndexError, AttributeError):
                print("click error")
        self.idle_time(idle_time_after_click)

    def type_in_xpath(self, xpath, text):
        id_found = False
        while not id_found:
            try:
                self.driver.find_element_by_xpath(xpath).clear()
                self.driver.find_element_by_xpath(xpath).send_keys(text)
                id_found = True
            except (IndexError, AttributeError):
                print("field error error")

    def get_att_in_xpath(self, xpath):
        start = datetime.now()
        id_found = False
        while not id_found:
            try:
                end = datetime.now()
                if timedelta.total_seconds(end - start) > 2:
                    self.click_xpath(xpath.split("/button")[0])
                att = (
                    self.driver.find_element_by_xpath(xpath)
                    .get_attribute("src")
                    .replace("/", "-")
                    .split("-")[-2]
                )
                id_found = True
            except (IndexError, AttributeError):
                # print("att error")
                pass
        return att
