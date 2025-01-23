import re
import json


def big_json_by_blocks(file_path):
    # Открываем файл с JSON-строкой
    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # Регулярное выражение для выделения отдельных объектов JSON
    pattern = r'\{.*?\}'
    matches = re.findall(pattern, data)

    print(f"Всего найдено {len(matches)} блоков JSON.")
    for block in matches:
        print(block, type(block))




    # return matches

def block_json_to_temp_file(json_data):
    with open('json_data/temp.json', 'w', encoding='utf-8') as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)




if __name__ == '__main__':
    file_path = 'json_data/mini.txt'
    matches = big_json_by_blocks(file_path)
    # block_json_to_temp_file(matches)
    #
    # with open(input_file_path, 'r', encoding='utf-8') as f:
    #     json_data = json.load(f)
    #     print(json_data)
    #     print(type(json_data))
    #
    #
    # with open('json_data/temp.json', 'r', encoding='utf-8') as f:
    #     new_json_data = json.load(f)
    #     print(new_json_data)
    #     print(type(new_json_data))
