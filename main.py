from pathlib import Path
from screeninfo import get_monitors
from datetime import datetime
from sys import platform


def save_csv():
    dt = datetime.now().replace(second=0, microsecond=0).strftime('%d.%m.%Y %H.%M')
    monitors = get_monitors()

    Path("mouse_data").mkdir(exist_ok=True)

    save_path = (r"mouse_data/" + dt +
                 " ({0} x {1})".format(monitors[0].width, monitors[0].height) +
                 ".csv")

    header = r"date|x|y|button_type|press_release|action_type|active_window"
    with open(save_path, "w") as file:
        with open("mouse_log.csv", "r+") as f:
            data = f.read()
            file.write(header + "\n" + data)

    print(Path(save_path).resolve())


class Main:
    def __init__(self):
        Path("mouse_log.csv").unlink(missing_ok=True)
        if platform == "win32":
            from Services.windows_mouse_logger import WindowsMouseLogger
            from Base.keyboard_base import KeyboardLoggerBase

            mouse_win_logger = WindowsMouseLogger()
            mouse_win_logger.start_listener()

            keyboard_win_logger = KeyboardLoggerBase()
            keyboard_win_logger.start_listener()
        else:
            from Services.linux_mouse_logger import LinuxMouseLogger

            linux_logger = LinuxMouseLogger()
            linux_logger.start_listener()
        save_csv()


if __name__ == "__main__":
    print("Your mouse actions are tracked!")
    print("To end tracking press the middle mouse button")
    Main()
    input("Press Enter to continue...")
