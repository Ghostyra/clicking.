import pandas as pd
import ctypes
import os
from datetime import datetime
from Mouselogger import Keylogger


def foo():
    columns = ["date", "x","y", "pres_releas", "button_type", "action_type", "active_window"]
    df = pd.read_csv("mouse_log.csv", sep=".", names=columns, encoding="cp1252")

    dt = datetime.now().replace(second=0, microsecond=0).strftime('%d.%m.%Y %H.%M')

    user = ctypes.windll.user32
    screensize = user.GetSystemMetrics(0), user.GetSystemMetrics(1)

    if not os.path.isdir("mouse_data"):
        os.mkdir("mouse_data")

    df.to_csv(r"mouse_data/" + dt +
              " ({0} x {1})".format(screensize[0], screensize[1]) +
              ".csv")


class Main:
    def __init__(self):
        Keylogger()
        foo()


if __name__ == "__main__":
    Main()