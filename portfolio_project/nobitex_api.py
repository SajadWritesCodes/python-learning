import requests, json


def current_price(symbol,currency):
    response = requests.get(f"https://apiv2.nobitex.ir/v3/orderbook/{symbol}IRT").json()
    response = float(response['lastTradePrice'])
    current_price = round(response/currency ,2)
    return current_price

def get_fiatcurrency_price(fiat='USDT'):
    fiat = requests.get(f"https://apiv2.nobitex.ir/v3/orderbook/{fiat}IRT").json()
    fiat = float(fiat['lastTradePrice'])
    return fiat
