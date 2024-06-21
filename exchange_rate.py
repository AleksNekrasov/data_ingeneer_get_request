import requests
import json

#  Example Request: https://v6.exchangerate-api.com/v6/79e8ba26d7e58f3e988dcaa0/latest/USD


key = f'79e8ba26d7e58f3e988dcaa0'

URL = f'https://v6.exchangerate-api.com/v6/{key}/latest/USD'

get_ex = f"https://v6.exchangerate-api.com/v6/{key}/pair/USD/RUB"

probe = f"https://v6.exchangerate-api.com/v6/{key}/pair/USD/RUB/AMOUNT"

r = requests.get(url=URL)

if r.status_code == 200:
    data = r.json()        # преобразуем json в вид словаря
    result = json.dumps(data, indent=4, ensure_ascii=False) # преобразуем в стринг

    list_valutes = data.get("conversion_rates").keys()
    print(result)
    print(f'Data type is: {(type(data))}')
    print(f'Result type is: {(type(result))}')
    print(list_valutes)
    print(type(list_valutes))
    #циклы написать





#result = r.json()
#print(result)
#print(json.dumps(result, indent=4, ensure_ascii=False))
print("------------------------------------------------------")
#f = requests.get(url=probe)
#resulter = f.json()
#print(json.dumps(resulter, indent=4, ensure_ascii=False))
#print(result.get('conversion_rates').get("RUB"))
