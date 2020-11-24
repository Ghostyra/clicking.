import pandas as pd
import os
from screeninfo import get_monitors
from datetime import datetime
from sys import platform


def foo():
    columns = ["date", "x", "y", "press_release", "button_type", "action_type", "active_window"]
    df = pd.read_csv("mouse_log.csv", sep=".", names=columns, encoding="cp1252")

    dt = datetime.now().replace(second=0, microsecond=0).strftime('%d.%m.%Y %H.%M')

    monitors = get_monitors()

    if not os.path.isdir("mouse_data"):
        os.mkdir("mouse_data")

    save_path = (r"mouse_data/" + dt +
                 " ({0} x {1})".format(monitors[0].width, monitors[0].height) +
                 ".csv")
    df.to_csv(save_path)
    print(os.path.abspath(save_path))


class Main:
    def __init__(self):
        if os.path.isfile("mouse_log.csv"):
            os.remove("mouse_log.csv")
        if platform == "win32":
            from Services.windows_mouse_logger import WindowsMouseLogger
            WindowsMouseLogger()
        else:
            from Services.linux_mouse_logger import LinuxMouseLogger
            LinuxMouseLogger()
        foo()


if __name__ == "__main__":
    print("Your mouse actions are tracked!")
    print("To end tracking press the middle mouse button")
    Main()
    input("Press Enter to continue...")
