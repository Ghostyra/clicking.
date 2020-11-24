from typing import Optional
import Xlib
import Xlib.display

from Base.mouselogger_base import MouseLoggerBase


class LinuxMouseLogger(MouseLoggerBase):
    pass

    def __init__(self):
        super().__init__()

    def get_foreground_window_title(self) -> Optional[str]:
        display = Xlib.display.Display()
        window = display.get_input_focus().focus
        wm_class = window.get_wm_class()
        if wm_class is None:
            window = window.query_tree().parent
            wm_class = window.get_wm_class()
        winclass = wm_class[1]
        return winclass
