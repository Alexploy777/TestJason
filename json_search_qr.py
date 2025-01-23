import json


class JsonSearch:
    def __init__(self, json_file_name, sign_of_qr, sign_for_search_list):
        self.json_data = None
        self.json_reading(json_file_name)
        self.sign_of_qr = sign_of_qr
        self.sign_for_search_list = sign_for_search_list

    def json_reading(self, json_file_name):
        with open(json_file_name, 'r', encoding='utf-8') as f:
            text_data = f.read()
            text_data = text_data.replace('][', ',')
            json_data = json.loads(text_data)
            # json_data = json.load(f)
        self.json_data = json_data


    def decoder(self, string):
        return string.encode('latin1').decode('utf-8')


    def get_status_mod(self):
        global new_json_data
        qr_data_dic = {}

        for block in self.json_data:
            dic_of_block = block["cisInfo"]
            requestedCis = dic_of_block[self.sign_of_qr]
            if 'status' in dic_of_block:
                qr_data_dic[requestedCis] = dic_of_block['status']
            else:
                qr_data_dic[requestedCis] = self.decoder(block['errorMessage'])

        self.qr_data_dic = qr_data_dic
        self.write_to_file()

    def write_to_file(self):
        with open('qr_data_result.json', 'w', encoding='utf-8') as f:
            json.dump(self.qr_data_dic, f, ensure_ascii=False, indent=4)




if __name__ == '__main__':
    file = 'json_data/check_short.txt'  # файл с json
    # file = 'json_data/answer_mini.json'  # файл с json
    sign_of_qr = 'cis'  # ключ индентификатора QR
    sign_for_search_list = ["status", "errorMessage"]
    jsonsearch = JsonSearch(file, sign_of_qr, sign_for_search_list)
    result = jsonsearch.get_status_mod()
    # for r in result:
    #     print(f'QR: {r} --> результат: {result[r]}')
