import re
import json

def process_json(file_path, batch_size=1000):
    # Открываем файл с JSON-строкой
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Регулярное выражение для выделения отдельных объектов JSON
    pattern = r'\{.*?\}'
    matches = re.findall(pattern, data)

    print(f"Всего найдено {len(matches)} блоков JSON.")

    # return

    # Обработка порциями
    for i in range(0, len(matches), batch_size):
        batch = matches[i:i + batch_size]
        try:
            # Преобразуем порцию в JSON
            parsed_batch = [json.loads(item) for item in batch]
            print(f"Обработка блоков {i} - {i + len(parsed_batch)}...")
            # Здесь выполняем обработку parsed_batch
            process_batch(parsed_batch)
        except json.JSONDecodeError as e:
            print(f"Ошибка в блоках {i} - {i + batch_size}: {e}")

def process_batch(batch):
    # Пример обработки блока
    for item in batch:
        cis = item.get("cisInfo", {}).get("cis", "Нет данных")
        print(f"Обрабатывается: {cis}")

# Пример вызова функции
process_json("json_data/check_short.json", batch_size=1000)





if __name__ == '__main__':
    file_path = 'json_data/check_short.json'
