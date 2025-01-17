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
    JSON = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3,
                'f': 'найдено',
                'xxg': {4: 44, 'i': 'также_найдено 1'},
            }
        },
        'список': [
            {'g': 4},
            {'h': 5, 'i': 'также_найдено 2'}
        ]
    }

    jsonsearch = JsonSearch(JSON)
    jsond_search = jsonsearch.jsond_search_all

    result1 = jsond_search('f')  # Вывод: ['найдено']
    print(result1)
    result2 = jsond_search('i')  # Вывод: ['также_найдено 2', 'также_найдено']
    print(result2)
    result3 = jsond_search('x')  # Вывод: []
    print(result3)
