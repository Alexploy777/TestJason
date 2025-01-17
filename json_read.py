import json
import pprint


JSON = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3,
            'f': 'найдено',
            'xxg': {4: 44, 'i': 'также_найдено 2'},
        }
    },
    'список': [
        {'g': 4},
        {'h': 5, 'i': 'также_найдено'}
    ]
}

# json_data = json.loads(JSON)



# def jsond_seach(data, key):
#     for k, v in data.items():
#         if k == key:
#             return v
#         if isinstance(v, dict):
#             return jsond_seach(v, key)
#         elif isinstance(v, list):
#             for item in v:
#                 if isinstance(item, dict):
#                     return jsond_seach(item, key)

def jsond_seach_all(data, key):
    results = []
    for k, v in data.items():
        if k == key:
            results.append(v)
        if isinstance(v, dict):
            results.extend(jsond_seach_all(v, key))
        elif isinstance(v, list):
            for item in v:
                if isinstance(item, dict):
                    results.extend(jsond_seach_all(item, key))
    return results

result1 = jsond_seach_all(JSON, 'f')  # Вывод: 'найдено'
print(result1)
result2 = jsond_seach_all(JSON, 'i')  # Вывод: 'также_найдено'
print(result2)
result3 = jsond_seach_all(JSON, 'x')  # Вывод: None
print(result3)


if __name__ == '__main__':
    pass