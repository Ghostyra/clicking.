import logging
from pynput.mouse import Button
from pynput import mouse


class MouseLoggerBase(object):
    def __init__(self):
        self.buttons_dict = {Button.left: "left", Button.right: "right"}
        self.logging = logging
        self.logging.basicConfig(filename="mouse_log.csv", level=logging.INFO, format="%(asctime)s|%(message)s")

    def get_foreground_window_title(self):
        raise NotImplemented

    def on_move(self, x, y):
        self.logging.info("{0}|{1}|None|None|Move|".format(x, y) + self.get_foreground_window_title())

    def on_click(self, x, y, button, pressed):
        if button == Button.middle:
            return False
        self.logging.info("{0}|{1}|{2}|{3}|".format(x, y, self.buttons_dict[button], (
            "pressed" if pressed else "released")) + "click|" + self.get_foreground_window_title())

    def listener(self):
        with mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click) as listener:
            listener.join()
