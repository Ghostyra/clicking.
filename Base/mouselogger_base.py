from pynput.mouse import Button
from pynput import mouse
from abc import abstractmethod
import logging
import threading


class MouseLoggerBase:
    def __init__(self):
        self.buttons_dict = {Button.left: "left", Button.right: "right", Button.middle: "middle"}
        self.logging = logging
        self.logging.basicConfig(filename="mouse_log.csv", level=logging.INFO, format="%(asctime)s|%(message)s")
        self.listener_mouse = mouse.Listener(on_move=self.on_move,
                                             on_click=self.on_click)

    @abstractmethod
    def get_foreground_window_title(self):
        pass

    def on_move(self, x, y):
        if threading.active_count() == 2:
            self.listener_mouse.stop()
        self.logging.info("{0}|{1}|None|None|Move|".format(x, y) + self.get_foreground_window_title())

    def on_click(self, x, y, button, pressed):
        self.logging.info("{0}|{1}|{2}|{3}|".format(x, y, self.buttons_dict[button], (
            "pressed" if pressed else "released")) + "click|" + self.get_foreground_window_title())

    def start_listener(self):
        self.listener_mouse.start()

    def join_listener(self):
        self.listener_mouse.join()
