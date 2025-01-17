import json


class JsonSearch:
    def __init__(self, json_data):
        self.json_data = json_data

    def jsond_search_all(self, key, data=None):
        if data is None:
            data = self.json_data

        results = []
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    results.append(v)
                if isinstance(v, (dict, list)):
                    results.extend(self.jsond_search_all(key, v))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    results.extend(self.jsond_search_all(key, item))
        return results


if __name__ == '__main__':
    # json_file_name = 'json_data/exsample.json'
    json_file_name = 'json_data/answer1.json'
    with open(json_file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    jsonsearch = JsonSearch(data)
    jsond_search = jsonsearch.jsond_search_all

    # result1 = jsond_search('f')  # Вывод: ['найдено']
    # print(result1)
    result2 = jsond_search('cis')  # Вывод: ['также_найдено 2', 'также_найдено']
    print(result2)
    # result3 = jsond_search('x')  # Вывод: []
    # print(result3)
