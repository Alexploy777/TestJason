import requests
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives import hashes
from base64 import b64encode

# URL для авторизации
url = "https://markirovka.crpt.ru/api/v3/true-api/auth"

# Уникальный идентификатор
uuid = "fc594ac1-a643-413c-870a-7a60e192d57f"

# Строка данных для подписи
data = "строка данных для подписи"  # Узнайте актуальное значение в документации

# Загрузка закрытого ключа (пример PEM-файла)
private_key_path = "path/to/private_key.pem"  # Укажите путь к закрытому ключу
with open(private_key_path, "rb") as key_file:
    private_key = load_pem_private_key(key_file.read(), password=None)

# Создание подписи
signature = private_key.sign(
    data.encode(),
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Кодирование подписи в Base64
signature_base64 = b64encode(signature).decode()

# Тело запроса
payload = {
    "uuid": uuid,
    "data": data,
    "signature": signature_base64
}

# Заголовки
headers = {
    "Content-Type": "application/json",
    "accept": "application/json"
}

# Выполнение запроса
try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("Токен успешно получен!")
        print("Ответ сервера:", response.json())  # Токен будет в ответе
    else:
        print("Ошибка авторизации.")
        print(f"Код статуса: {response.status_code}")
        print("Ответ:", response.text)
except requests.exceptions.RequestException as e:
    print("Ошибка соединения:", e)
