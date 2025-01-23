import json


class JsonSearch:
    def __init__(self, json_file_name, sign_of_qr, sign_for_search_list):
        self.json_data = None
        self.json_reading(json_file_name)
        self.sign_of_qr = sign_of_qr
        self.sign_for_search_list = sign_for_search_list

    def json_reading(self, json_file_name):
        with open(json_file_name, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            # correct_text = text.encode('latin1').decode('utf-8')
            # correct_data = json.loads(correct_text)

        self.json_data = json_data

    def json_search_by_key(self, key, data=None):
        if data is None:
            data = self.json_data

        results = []
        if isinstance(data, dict):
            for k, v in data.items():
                if k == key:
                    results.append(v)
                if isinstance(v, (dict, list)):
                    results.extend(self.json_search_by_key(key, v))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    results.extend(self.json_search_by_key(key, item))
        return results

    def get_status_mod(self):
        global new_json_data
        qr_data_dic = {}
        qr_values_list = []

        for block in self.json_data:
            key_block = block["result"][self.sign_of_qr]
            for sign_for_search in self.sign_for_search_list:
                val = self.json_search_by_key(sign_for_search)
                qr_values_list.append(val)
            qr_data_dic[key_block] = qr_values_list

        return qr_data_dic


if __name__ == '__main__':
    file = 'json_data/answer1.json'  # файл с json
    # input_file_path = 'json_data/answer1.json'
    sign_of_qr = 'cis'  # ключ индентификатора QR
    sign_for_search_list = ["status", "errorMessage"]
    jsonsearch = JsonSearch(file, sign_of_qr, sign_for_search_list)
    result = jsonsearch.get_status_mod()
    for r in result:
        print(r)
        print('-------------------------')
        for item in result[r]:
            print(item)
        print('-------------------------')