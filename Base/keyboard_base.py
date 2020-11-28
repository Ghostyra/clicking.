from pynput import keyboard


class KeyboardLoggerBase:
    def __init__(self):
        self.listener_keyboard = keyboard.GlobalHotKeys({'<ctrl>+<alt>+h': self.stop_threads})

    def stop_threads(self):
        self.listener_keyboard.stop()

    def start_listener(self):
        self.listener_keyboard.start()

    def join_listener(self):
        self.listener_keyboard.join()
