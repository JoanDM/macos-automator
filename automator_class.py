import ast
import smtplib
import ssl
import subprocess
from datetime import datetime, timedelta

from beepy import beep
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
from pynput.mouse import Button
from pynput.mouse import Controller as MouseController
from requests_html import HTMLSession
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from config import (
    _chromedriver_pathlib,
    _default_receiver_email,
    _default_sender_email,
    _gmail_app_password,
)


class Automator(object):
    def __init__(self):
        self.mouse = MouseController()
        self.keyboard = KeyboardController()
        self.driver = None
        self.html_session = None

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

    def search_spotlight_and_launch(self, text):
        with self.keyboard.pressed(Key.cmd):
            self.idle_time(0.5)
            self.keyboard.press(Key.space)
            self.keyboard.release(Key.space)
        self.keyboard.release(Key.cmd)
        self.idle_time(1)
        self.keyboard.type(text)
        self.idle_time(3)
        self.press_enter()
        self.idle_time(3)

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

    def press_space(self):
        self.keyboard.press(Key.space)

    def press_backspace(self):
        self.keyboard.press(Key.backspace)

    def press_shift_key(self):
        self.keyboard.press(Key.shift)

    def press_cmd_key(self):
        self.keyboard.press(Key.cmd)

    def press_alt_key(self):
        self.keyboard.press(Key.alt)

    def release_cmd_key(self):
        self.keyboard.release(Key.cmd)

    def release_shift_key(self):
        self.keyboard.release(Key.shift)

    def release_alt_key(self):
        self.keyboard.release(Key.alt)

    def press_enter(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)
        self.idle_time(0.5)

    def press_cmd_tab(self, idle_time=0.2):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.tab)
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.tab)
        self.idle_time(idle_time)

    def press_refresh_key(self, idle_time=1.5):
        self.keyboard.press(Key.cmd)
        self.keyboard.press("r")
        self.keyboard.release(Key.cmd)
        self.keyboard.release("r")
        self.idle_time(idle_time)

    def press_save_shortcut(self):
        self.keyboard.press(Key.cmd)
        self.keyboard.press(Key.shift)
        self.idle_time(1)
        self.keyboard.press("s")
        self.keyboard.release("s")
        self.keyboard.release(Key.cmd)
        self.keyboard.release(Key.shift)
        self.idle_time(4)

    def press_right_arrow(self):
        self.keyboard.press(Key.right)

    def press_left_arrow(self):
        self.keyboard.press(Key.left)

    def press_down_arrow(self):
        self.keyboard.press(Key.down)

    def erase_character(self):
        self.keyboard.press(Key.backspace)
        self.keyboard.release(Key.backspace)
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

    def start_html_session(self):
        self.html_session = HTMLSession()

    def close_html_session(self):
        self.html_session.close()

    def send_email(self, subject, content):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = _default_sender_email  # Enter your address
        receiver_email = _default_receiver_email  # Enter receiver address
        password = _gmail_app_password
        message = f"Subject: {subject}\n\n{content}"

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    def send_html_post_request(
        self, url, json_payload, headers, timeout=5, res_status_code=None
    ):
        res = None
        if res_status_code is not None:
            try:
                res = self.html_session.request(
                    method="POST",
                    url=url,
                    json=json_payload,
                    headers=headers,
                    timeout=timeout,
                )
                if res is not None and res.status_code == res_status_code:
                    # print("\nSuccessful request!")
                    pass
                else:
                    print("\nInvalid response to POST...")
            except:
                print("Connection error on POST request...")
                self.idle_time(timeout)
        else:
            res = self.html_session.request(
                method="POST",
                url=url,
                json=json_payload,
                headers=headers,
                timeout=timeout,
            )

        return res

    def send_get_html_request(self, url, timeout=5, res_status_code=None):
        res = None
        if res_status_code is not None:
            try:
                res = self.html_session.request(method="GET", url=url, timeout=timeout)
                # res = self.html_session.get(url=url, timout=5)
                if res is not None and res.status_code == res_status_code:
                    # print("\nSuccessful request!")
                    pass
                else:
                    print("\nInvalid response to GET...")
            except:
                print("Connection error on GET request...")
                self.idle_time(timeout)
        else:
            res = self.html_session.get(url=url)

        return res
