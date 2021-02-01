from pathlib import Path
from screeninfo import get_monitors
from datetime import datetime
from sys import platform


# Saving the received information, screen resolution, and date
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
        from Base.keyboard_base import KeyboardLoggerBase

        Path("mouse_log.csv").unlink(missing_ok=True)
        keyboard_logger = KeyboardLoggerBase()
        keyboard_logger.start_listener()

        # Implementation for different OS
        if platform == "win32":
            from Services.windows_mouse_logger import WindowsMouseLogger

            mouse_win_logger = WindowsMouseLogger()
            mouse_win_logger.start_listener()

            mouse_win_logger.join_listener()
            keyboard_logger.join_listener()
        else:
            from Services.linux_mouse_logger import LinuxMouseLogger

            mouse_linux_logger = LinuxMouseLogger()
            mouse_linux_logger.start_listener()

            mouse_linux_logger.join_listener()
            keyboard_logger.join_listener()

        save_csv()


if __name__ == "__main__":
    print("Your mouse actions are tracked!")
    print("To end tracking press <ctrl>+<alt>+h")
    Main()
    input("Press Enter to continue...")
