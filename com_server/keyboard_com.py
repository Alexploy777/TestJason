import ctypes
import pythoncom
import keyboard
import sys
from win32com.server.register import RegisterClasses, UnregisterClasses
from win32com.server.util import wrap

user32 = ctypes.WinDLL('user32', use_last_error=True)

KLF_ACTIVATE = 0x00000001
MAPVK_VSC_TO_VK = 1  # Преобразование сканкода в виртуальный код

# Загрузка английской раскладки
english_layout = user32.LoadKeyboardLayoutW("00000409", KLF_ACTIVATE)


def to_english(vk, scan, shift_pressed):
    buffer = ctypes.create_unicode_buffer(8)
    keyboard_state = (ctypes.c_ubyte * 256)()

    if shift_pressed:
        keyboard_state[0x10] = 0x80

    n_chars = user32.ToUnicodeEx(
        vk,
        scan,
        keyboard_state,
        buffer,
        ctypes.sizeof(buffer) // ctypes.sizeof(ctypes.c_wchar),
        0,
        english_layout
    )
    if n_chars > 0:
        return buffer.value[:n_chars]
    return ''


class KeyboardInterceptor:
    _public_methods_ = ["StartListening", "GetLastChar"]
    _reg_progid_ = "KeyboardInterceptor.QRHelper"
    _reg_clsid_ = "{9F3FBB4D-FAF3-4C73-82A6-D8A8C8A7C2D1}"

    def __init__(self):
        self.last_char = ""
        self.new_char_available = False  # Флаг, чтобы обработать каждый символ только один раз
        keyboard.hook(self.on_key_event)

    def on_key_event(self, event):
        if event.event_type != 'down':
            return

        scan = event.scan_code
        vk = user32.MapVirtualKeyW(scan, MAPVK_VSC_TO_VK)
        shift_pressed = keyboard.is_pressed('shift')
        char = to_english(vk, scan, shift_pressed)
        if char:
            self.last_char = char
            self.new_char_available = True  # Флаг, что есть новый символ

    def StartListening(self):
        """Запускает обработку клавиш в фоне"""
        print("Перехват запущен. Для выхода нажмите ESC.")
        keyboard.wait('esc')

    def GetLastChar(self):
        """Возвращает последний введенный символ в английской раскладке один раз"""
        if self.new_char_available:
            self.new_char_available = False  # Сброс флага, чтобы не повторялся
            return self.last_char
        return ""  # Если нет нового символа, возвращаем пустую строку


if __name__ == '__main__':
    if "--register" in sys.argv:
        print("Регистрация COM-объекта...")
        RegisterClasses(KeyboardInterceptor)
        print("COM-объект зарегистрирован.")
    elif "--unregister" in sys.argv:
        print("Удаление COM-объекта...")
        UnregisterClasses(KeyboardInterceptor)
        print("COM-объект удален.")
    else:
        print("Запуск COM-сервера...")
        pythoncom.CoInitialize()
        obj = wrap(KeyboardInterceptor())
        pythoncom.PumpMessages()
