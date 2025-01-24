import os


def split_large_file_without_regex(input_file_path, output_dir, block_size):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        elements = content.split("},")  # Разделяем данные по запятой

        print(elements)

        print(len(elements))
        part_counter = 1

        for i in range(0, len(elements), block_size):
            block = "},".join(elements[i:i+block_size]) + "},"
            output_file_path = f"{output_dir}/part_{part_counter}.txt"
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write('[' + block + ']')
            print(f"Часть {part_counter} сохранена в {output_file_path}")
            part_counter += 1


input_file = 'json_data/mini.txt'
# input_file = 'json_data/check_short.json'

output_dir = 'json_data/output'  # Папка для сохранения частей

split_large_file_without_regex(input_file, output_dir, block_size=10)