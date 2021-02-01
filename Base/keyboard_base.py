from pynput import keyboard


# Keyboard-logger class
class KeyboardLoggerBase:
    def __init__(self):
        self.listener_keyboard = keyboard.GlobalHotKeys({'<ctrl>+<alt>+h': self.stop_threads})

    # Stop thread
    def stop_threads(self):
        self.listener_keyboard.stop()

    # Start thread
    def start_listener(self):
        self.listener_keyboard.start()

    # Join thread
    def join_listener(self):
        self.listener_keyboard.join()
