import win32com.client
import time

def main():
    try:
        interceptor = win32com.client.Dispatch("KeyboardInterceptor.QRHelper")
    except Exception as e:
        print("Ошибка: COM-сервер 'KeyboardInterceptor.QRHelper' не запущен.")
        print("Запустите сервер перед использованием.")
        return

    print("Ожидание ввода...")
    while True:
        char = interceptor.GetLastChar()
        if char:  # Печатаем только если есть новый символ
            print(f"Символ: {char}")
        time.sleep(0.05)  # Уменьшаем задержку

if __name__ == '__main__':
    main()
