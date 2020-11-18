import logging
from pynput.mouse import Button
from pynput import mouse
from ctypes import windll, create_unicode_buffer
from typing import Optional

class Keylogger:
    def __init__(self):
        logging.basicConfig(filename="mouse_log.csv", level=logging.INFO, format="%(asctime)s.%(message)s")
        self.listener()

    def get_foreground_window_title(self) -> Optional[str]:
        hWnd = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(hWnd)
        buf = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hWnd, buf, length + 1)

        return buf.value if buf.value else "None"

    def on_move(self, x, y):
        logging.info("{0}.{1}.None.None.Move.".format(x, y) + self.get_foreground_window_title())

    def on_click(self, x, y, button, pressed):
        if button == Button.left:
            logging.info("{0}.{1}.{2}.left.Click.".format(x, y, ("pressed" if pressed else "released")) + self.get_foreground_window_title())
        elif button == Button.right:
            logging.info("{0}.{1}.{2}.right.Click.".format(x, y, ("pressed" if pressed else "released")) + self.get_foreground_window_title())
        elif button == Button.middle:
            return False

    def listener(self):
        with mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click) as listener:
                listener.join()