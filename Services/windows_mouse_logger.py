from ctypes import windll, create_unicode_buffer

from Base.mouselogger_base import MouseLoggerBase


class WindowsMouseLogger(MouseLoggerBase):
    def __init__(self):
        super().__init__()

    def get_foreground_window_title(self):
        h_wnd = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(h_wnd)
        buf = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(h_wnd, buf, length + 1)
        return buf.value if buf.value else "None"


