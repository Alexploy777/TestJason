import re
import os


def split_file_by_pattern(input_file_path, output_dir, pattern):
    # Убедимся, что папка для выходных файлов существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Читаем содержимое файла
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Находим все совпадения согласно паттерну
    matches = list(re.finditer(pattern, content))
    processed_length = 0  # Длина обработанной части контента

    # Создаём файлы по найденным блокам
    for i, match in enumerate(matches):
        part_content = '[' + match.group(0) + ']'  # Берём совпавший текст
        processed_length += len(part_content)  # Увеличиваем счётчик обработанной длины

        output_file_path = f"{output_dir}/part_{i + 1}.txt"
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(part_content)
            print(f"Часть {i + 1} сохранена в {output_file_path}")

    # Обрабатываем оставшийся текст, если он есть
    remaining_content = content[processed_length:].strip()
    if remaining_content:
        output_file_path = f"{output_dir}/part_{len(matches) + 1}.txt"
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write('[' + remaining_content + ']')
            print(f"Оставшаяся часть сохранена в {output_file_path}")


# Пример использования
pattern = r'(\{(.*?)\},){10}'  # Паттерн для поиска блоков
input_file = 'json_data/check_short.json'  # Входной файл
output_directory = 'json_data/output'  # Папка для сохранения частей

split_file_by_pattern(input_file, output_directory, pattern)
