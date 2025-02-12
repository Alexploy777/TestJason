from PyQt5.QtWidgets import QApplication, QLineEdit, QVBoxLayout, QWidget


class DateTimeInput(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaxLength(19)  # Формат: YYYY-mm-dd HH:MM:SS (19 символов)
        self.setPlaceholderText("Введите дату и время: YYYY-mm-dd HH:MM:SS")
        self.textChanged.connect(self.format_input)  # Событие изменения текста

    def format_input(self, text):
        # Сохраняем текущую позицию курсора
        cursor_position = self.cursorPosition()

        # Удаляем все символы, кроме цифр
        digits = ''.join(filter(str.isdigit, text))

        # Формируем дату и время в формате YYYY-mm-dd HH:MM:SS
        formatted = ""
        if len(digits) > 0:
            formatted += digits[:4]  # Год
        if len(digits) > 4:
            formatted += "-" + digits[4:6]  # Месяц
        if len(digits) > 6:
            formatted += "-" + digits[6:8]  # День
        if len(digits) > 8:
            formatted += " " + digits[8:10]  # Часы
        if len(digits) > 10:
            formatted += ":" + digits[10:12]  # Минуты
        if len(digits) > 12:
            formatted += ":" + digits[12:14]  # Секунды

        # Обновляем текст в поле
        self.blockSignals(True)  # Отключаем сигналы, чтобы избежать рекурсии
        self.setText(formatted)

        # Корректируем позицию курсора
        # Если курсор находится после добавленного разделителя, сдвигаем его вправо
        if cursor_position < len(formatted) and formatted[cursor_position - 1] in "- :":
            cursor_position += 1
        self.setCursorPosition(min(cursor_position, len(formatted)))

        self.blockSignals(False)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.lineEdit_corrected = DateTimeInput(self)
        layout.addWidget(self.lineEdit_corrected)

        self.setLayout(layout)
        self.setWindowTitle("Ввод даты и времени")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
