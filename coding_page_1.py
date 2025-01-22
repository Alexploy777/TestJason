import json

# text = "ÐÐ/ÐÐ Ð½Ðµ Ð½Ð°Ð¹Ð´ÐµÐ½"
# text = "productGroup"

# correct_text = text.encode('latin1').decode('utf-8')
# print(correct_text)  # "КМ/КИ не найден"


with open('json_data/answer_mini.json', encoding='utf-8') as file:
    text = file.read()
    correct_text = text.encode('latin1').decode('utf-8')
    data = json.loads(correct_text)

# with open('json_data/answer_mini.json', 'r', encoding='utf-8') as f:
#     text = json.load(f)

# correct_text = text.encode('latin1').decode('utf-8')

print(data)


if __name__ == '__main__':
    pass