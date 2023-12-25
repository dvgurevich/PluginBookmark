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

    # Перемещаемся к следующей закладке
    def goto_next_bookmark(self):
        current_position = self.mouse.position
        next_bookmark = None
        for bookmark in self.bookmarks:
            if bookmark[1] > current_position[1]:
                next_bookmark = bookmark
                self.mouse.position = next_bookmark
                break
        if next_bookmark:
            print(f"Moving to bookmark at position {next_bookmark}")
        else:
            print("No more bookmarks")

    # Перемещаемся к предыдущей закладке
    def goto_previous_bookmark(self):
        current_position = self.mouse.position
        next_bookmark = None
        for bookmark in self.bookmarks:
            if bookmark[1] < current_position[1]:
                next_bookmark = bookmark
                self.mouse.position = next_bookmark
                break
        if next_bookmark:
            print(f"Moving to bookmark at position {next_bookmark}")
        else:
            print("No more bookmarks")

    # Функции обработчики нажатий клавиш
    def on_ctrl_shift_h(self, event):
        if keyboard.is_pressed("ctrl+shift+h"):
            self.save_cursor_position()

    def on_ctrl_shift_s(self, event):
        if keyboard.is_pressed("ctrl+shift+s"):
            self.goto_next_bookmark()

    def on_ctrl_shift_d(self, event):
        if keyboard.is_pressed("ctrl+shift+d"):
            self.goto_previous_bookmark()

    def start(self):
        keyboard.on_press(self.on_ctrl_shift_d)
        keyboard.on_press(self.on_ctrl_shift_s)
        keyboard.on_press(self.on_ctrl_shift_h)
        keyboard.wait()


my_plugin = MyPlugin()
