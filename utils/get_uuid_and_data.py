import requests


# {'uuid': 'fc594ac1-a643-413c-870a-7a60e192d57f', 'data': 'QEUQNYUUBXRVAHMISMFNAQJVAZPQUE'}


url = 'https://markirovka.crpt.ru/api/v3/true-api/auth/key'

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

data = {'uuid': 'fc594ac1-a643-413c-870a-7a60e192d57f', 'data': 'QEUQNYUUBXRVAHMISMFNAQJVAZPQUE'}

response = requests.get(url, headers=headers)



print(response)
print(response.json())



if __name__ == '__main__':
    pass