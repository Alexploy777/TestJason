import json


class JsonSearch:
    def __init__(self, json_file_name, sign_of_qr):
        self.json_reading(json_file_name)
        self.sign_of_qr = sign_of_qr

    def json_reading(self, json_file_name):
        with open(json_file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.json_data = data

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
        # print(results)
        return results

    # def json_search_by_value(self, value, data=None):
    #     """Поиск всех ключей по указанному значению."""
    #     if data is None:
    #         data = self.json_data
    #
    #     results = []
    #     if isinstance(data, dict):
    #         for k, v in data.items():
    #             if v == value:
    #                 results.append(k)
    #             if isinstance(v, (dict, list)):
    #                 results.extend(self.json_search_by_value(value, v))
    #     elif isinstance(data, list):
    #         for item in data:
    #             if isinstance(item, (dict, list)):
    #                 results.extend(self.json_search_by_value(value, item))
    #     return results


    def get_status(self, qr_list):
        global new_json_data
        qr_data_dic = {}

        for qr_string in qr_list:
            for item in self.json_data:
                value = item['result'][self.sign_of_qr]
                if value == qr_string:
                    new_json_data = item
                    qr_data = self.json_search_by_key('status', new_json_data)
                    qr_data_dic[qr_string] = qr_data[0]
        return qr_data_dic



if __name__ == '__main__':
    # file = 'json_data/exsample.json'
    file = 'json_data/answer1.json' # файл с json
    sign_of_qr = 'cis'  # ключ индентификатора QR

    qr_list = ["string-abracodabra_bla_bla_орпорпор", "ррлдорлоршгрлгрлорл"] # QRs


    jsonsearch = JsonSearch(file, sign_of_qr)
    r = jsonsearch.get_status(qr_list)
    print(r)




