import ijson


def process_large_json(file_path):
    # Словарь для хранения результатов
    qr_data_dic = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        # Считываем объекты из массива JSON
        for item in ijson.items(file, "item"):
            cis_info = item.get("cisInfo", {})
            requested_cis = cis_info.get("requestedCis", "")
            status = cis_info.get("status", None)
            error_message = item.get("errorMessage", None)

            if status:
                qr_data_dic[requested_cis] = status
            elif error_message:
                qr_data_dic[requested_cis] = error_message.encode('latin1').decode('utf-8')

    # print(qr_data_dic)
    return qr_data_dic

    # # Сохраняем результат в файл
    # with open('output.json', 'w', encoding='utf-8') as output_file:
    #     import json
    #     json.dump(qr_data_dic, output_file, ensure_ascii=False, indent=4)
    # print("Обработка завершена!")





if __name__ == '__main__':
    # file = 'json_data/answer_mini.json'
    file = 'json_data/check_short.json'
    # Вызов функции
    qr_data_dic = process_large_json(file)
    count = 0
    for data in qr_data_dic:
        if count > 10:
            break
        count += 1
        print(data, '-->', qr_data_dic[data])

