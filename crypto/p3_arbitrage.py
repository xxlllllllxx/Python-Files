import requests


def get_binance_price(symbol):
    base_url = 'https://api.binance.com/api/v3/ticker/price'
    params = {'symbol': symbol}

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return float(data['price'])
    else:
        return None


def get_binance_coins():
    base_url = 'https://api.binance.com/api/v3/exchangeInfo'

    response = requests.get(base_url)
    data = response.json()
    stables = ["USDT", "FDUSD", "TUSD", "BUSD", "BNB", "BTC", "ETH"]
    if response.status_code == 200:
        symbols = data.get('symbols', [])
        stable_coins = set()
        alt_coins = set()

        for symbol_info in symbols:
            base_asset = symbol_info.get('baseAsset', '')
            quote_asset = symbol_info.get('quoteAsset', '')

            if base_asset and quote_asset:
                if base_asset in stables:
                    stable_coins.add(base_asset)
                else:
                    alt_coins.add(base_asset)

                if quote_asset in stables:
                    stable_coins.add(quote_asset)
                else:
                    alt_coins.add(quote_asset)

        return list(stable_coins), list(alt_coins)
    else:
        return None, None


def calculate_profit(starting_amount, symbol1, symbol2, symbol3) -> list:
    try:
        isflipped = [False, False, False]
        price1 = get_binance_price(symbol1 + symbol2)
        if price1 is None:
            price1 = get_binance_price(symbol2 + symbol1)
            isflipped[0] = True
        price2 = get_binance_price(symbol2 + symbol3)
        if price2 is None:
            price2 = get_binance_price(symbol3 + symbol2)
            isflipped[1] = True
        price3 = get_binance_price(symbol3 + symbol1)
        if price3 is None:
            price3 = get_binance_price(symbol1 + symbol3)
            isflipped[2] = True

        intermediate_amount_1 = starting_amount * price1 if not isflipped[0] else starting_amount / price1
        intermediate_amount_2 = intermediate_amount_1 * price2 if not isflipped[1] else intermediate_amount_1 / price2
        final_amount = intermediate_amount_2 * price3 if not isflipped[2] else intermediate_amount_2 / price3

        return [intermediate_amount_1, intermediate_amount_2, final_amount]
    except:
        return [float(0), float(0), float(0)]


if __name__ == "__main__":
    pass
    # sample only
    # starting_amount = 5
    # symbol1 = 'USDT'
    # symbol2 = 'BTC'
    # symbol3 = 'BNB'

    # result = calculate_profit(starting_amount, symbol1, symbol2, symbol3)

    # print(f"Starting with  :       {starting_amount:.10f} {symbol1:5}")
    # print(f"Trade {symbol1:9}:       {starting_amount:.20f} {symbol1:5} -> {result[0]:.20f} {symbol2:5}")
    # print(f"Trade {symbol2:9}:       {result[0]:.20f} {symbol2:5} -> {result[1]:.20f} {symbol3:5}")
    # print(f"Trade {symbol3:9}:       {result[1]:.20f} {symbol3:5} -> {result[2]:.20f}  {symbol1:5}")
    # print(f"Total profit   :       {result[2] - starting_amount:.20f} {symbol1:5}")
    available_coins = get_binance_coins()

    if available_coins:
        print("List of available coins on Binance:")
        for coin in available_coins:
            print(coin)
    else:
        print("Failed to fetch the list of available coins.")
