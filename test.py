import ijson



def json_reading(json_file_name):
    json_data = []
    with open(json_file_name, 'r', encoding='utf-8') as f:
        # Читаем поток данных JSON
        counter = 0
        for block in ijson.items(f, "item"):
            print(counter)
            print(block)
            json_data.append(block)
            counter += 1
        return counter, json_data

# json_file_name = 'json_data/mini.txt'
json_file_name = 'json_data/check_short.json'

res = json_reading(json_file_name)
print(res[0])
print(res[1])