from pynput import keyboard
from pynput.keyboard import Key


class KeyboardLoggerBase:
    def __init__(self):
        self.listener_keyboard = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        if key == Key.caps_lock:
            self.listener_keyboard.stop()
        try:
            print(key.char)
            pass
        except AttributeError:
            pass

    def start_listener(self):
        self.listener_keyboard.start()
