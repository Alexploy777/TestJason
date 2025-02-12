import ctypes
import keyboard

# Загрузка библиотеки user32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Константы для загрузки раскладки и для MapVirtualKey
KLF_ACTIVATE = 0x00000001
MAPVK_VSC_TO_VK = 1  # Преобразование сканкода в виртуальный код

# Загружаем английскую (US) раскладку.
# "00000409" – идентификатор английской (США) раскладки.
english_layout = user32.LoadKeyboardLayoutW("00000409", KLF_ACTIVATE)


def to_english(vk, scan, shift_pressed):
    """
    Преобразует комбинацию виртуального кода (vk) и сканкода (scan)
    в символ согласно английской раскладке.
    """
    # Создаем буфер для результата (8 символов – более чем достаточно)
    buffer = ctypes.create_unicode_buffer(8)

    # Подготавливаем массив состояний клавиш (256 байт)
    keyboard_state = (ctypes.c_ubyte * 256)()

    # Если зажат Shift, выставляем соответствующий бит.
    if shift_pressed:
        # Виртуальный код VK_SHIFT = 0x10.
        keyboard_state[0x10] = 0x80

    # Вызываем ToUnicodeEx:
    # Функция принимает:
    #   vk             – виртуальный код клавиши,
    #   scan           – аппаратный (сканкод),
    #   keyboard_state – массив состояний клавиш,
    #   buffer         – буфер для символов,
    #   buflen         – размер буфера,
    #   flags          – дополнительные флаги (0),
    #   layout         – дескриптор раскладки клавиатуры.
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
    else:
        return ''


def on_key_event(event):
    """
    Обработчик события клавиатуры.
    При нажатии клавиши (event.event_type == 'down') происходит попытка получить символ по английской раскладке.
    """
    if event.event_type != 'down':
        return

    scan = event.scan_code

    # Вычисляем виртуальный код по сканкоду с помощью MapVirtualKeyW
    vk = user32.MapVirtualKeyW(scan, MAPVK_VSC_TO_VK)

    shift_pressed = keyboard.is_pressed('shift')

    # Преобразуем нажатую клавишу в символ по английской раскладке
    char = to_english(vk, scan, shift_pressed)
    if char:
        print(char, end='', flush=True)


if __name__ == '__main__':
    print("Перехват с преобразованием в английскую раскладку.")
    print("Для выхода ESC.")
    keyboard.hook(on_key_event)
    keyboard.wait('esc')
