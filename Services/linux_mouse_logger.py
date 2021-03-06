import Xlib
import Xlib.display

from Base.mouselogger_base import MouseLoggerBase


# Class implementation for Linux
class LinuxMouseLogger(MouseLoggerBase):
    def __init__(self):
        super().__init__()

    def get_foreground_window_title(self):
        display = Xlib.display.Display()
        window = display.get_input_focus().focus
        wm_class = window.get_wm_class()
        if wm_class is None:
            window = window.query_tree().parent
            wm_class = window.get_wm_class()
        winclass = wm_class[1]
        return winclass
