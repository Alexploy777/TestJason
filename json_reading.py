import json


def json_reading(json_file_name):
    with open(json_file_name, 'r', encoding='utf-8') as f:
        json_objects = f.readlines()
    json_data = [json.loads(line.strip()) for line in json_objects]
    return json_data


if __name__ == '__main__':
    # json_file_name = 'json_data/check_short.json'
    json_file_name = 'json_data/answer_mini.json'
    res = json_reading(json_file_name)
    count = 0
    for r in res:
        print(r)
        if count == 10:
            break
        count += 1