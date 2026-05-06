import requests

def main():
    get_nob_api()

def get_nob_api():
    response = requests.get("https://apiv2.nobitex.ir/v3/orderbook/BTCIRT")
    result = response.json()
    nice_looking_result = int(result['lastTradePrice'])
    print (f"The last price is {nice_looking_result:,} Rials . ")

if __name__ == "__main__" :
    main()