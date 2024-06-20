import requests
# https://apilayer.com/marketplace/exchangerates_data-api#documentation-tab - api площадка
import _json


api_key = "pbIabQqVSqpTp9yNi9ln7ULzSV0y8SDR"

#curl --request GET 'https://api.apilayer.com/currency_data/convert?base=USD&symbols=EUR,GBP,JPY&amount=5&date=2018-01-01' \
#--header 'apikey: YOUR API KEY'

r = requests.get(url=url)
result = r.json()
print(result)
