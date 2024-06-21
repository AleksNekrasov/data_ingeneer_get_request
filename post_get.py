import requests
# https://apilayer.com/marketplace/exchangerates_data-api#documentation-tab - api площадка
import _json
URL = f'https://api.apilayer.com/currency_data/convert?base=USD&symbols=EUR,GBP,JPY&amount=5&date=2024-01-01'

api_key = "pbIabQqVSqpTp9yNi9ln7ULzSV0y8SDR"

header = {'apikey': api_key}

#curl --request GET 'https://api.apilayer.com/currency_data/convert?base=USD&symbols=EUR,GBP,JPY&amount=5&date=2018-01-01' \
#--header 'apikey: api_key

r = requests.get(url=URL, headers=header)
result = r.json()
print(result)
