import json


class JsonSearch:
    def __init__(self, json_file_name, sign_of_qr, sign_for_search_list):
        self.json_data = None
        self.json_reading(json_file_name)
        self.sign_of_qr = sign_of_qr
        self.sign_status = sign_for_search_list[0]
        self.sign_erors = sign_for_search_list[1]

    def json_reading(self, json_file_name):
        with open(json_file_name, 'r', encoding='utf-8') as f:
            text_data = f.read()
            text_data = text_data.replace('][', ',')
            json_data = json.loads(text_data)
        self.json_data = json_data


    def decoder(self, string):
        return string.encode('latin1').decode('utf-8')

    def get_status(self):
        global new_json_data
        qr_data_dic = {}

        for block in self.json_data:
            dic_of_block = block["cisInfo"]
            requestedCis = dic_of_block[self.sign_of_qr]
            if self.sign_status in dic_of_block:
                qr_data_dic[requestedCis] = dic_of_block[self.sign_status]
            else:
                qr_data_dic[requestedCis] = self.decoder(block[self.sign_erors])

        self.qr_data_dic = qr_data_dic
        self.write_to_file()
        print('Обработка завершена!')

    def write_to_file(self):
        with open('qr_data_result.json', 'w', encoding='utf-8') as f:
            json.dump(self.qr_data_dic, f, ensure_ascii=False, indent=0)


if __name__ == '__main__':
    input_file_path = 'json_data/check_short.txt'  # файл с json
    # input_file_path = 'json_data/answer_mini.json'  # файл с json
    sign_of_qr = 'cis'  # ключ индентификатора QR
    sign_for_search_list = ["status", "errorMessage"]
    jsonsearch = JsonSearch(input_file_path, sign_of_qr, sign_for_search_list)
    result = jsonsearch.get_status()
