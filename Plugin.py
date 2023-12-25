import keyboard
from pynput.mouse import Controller


class MyPlugin:
    def __init__(self):
        self.bookmarks = []
        self.mouse = Controller()
        self.start()

    # Сохраняем позицию курсора
    def save_cursor_position(self):
        cursor_position = self.mouse.position
        self.bookmarks.append(cursor_position)
        print(f"Bookmark created at position {cursor_position}")


    # Функции обработчики нажатий клавиш
    def on_ctrl_shift_h(self, event):
        if keyboard.is_pressed("ctrl+shift+h"):
            self.save_cursor_position()


    def start(self):
        keyboard.on_press(self.on_ctrl_shift_h)
        keyboard.wait()


my_plugin = MyPlugin()
