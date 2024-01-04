import requests

value_log = [None, None, None]


def manual_value(value: list = [None, None, None]):
    global value_log
    if value[0] is not None:
        value_log = value
    return value_log


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


def get_binance_prices(symbols):
    base_url = 'https://api.binance.com/api/v3/ticker/price'
    response = requests.get(base_url)
    data = response.json()
    if response.status_code == 200:
        prices = {}
        for entry in [entry for entry in data if entry['symbol'] in symbols]:
            symbol = entry['symbol']
            prices[symbol] = float(entry['price'])
        return prices
    else:
        return None


def calculate_profit(starting_amount, sy1, sy2, sy3) -> list:
    try:
        symbol1 = sy1.upper()
        symbol2 = sy2.upper()
        symbol3 = sy3.upper()
        symbol_pairs = [symbol1 + symbol2, symbol2 + symbol3, symbol3 + symbol1, symbol2 + symbol1, symbol3 + symbol2, symbol1 + symbol3]

        prices = get_binance_prices(symbol_pairs)

        # Initialize isflipped list
        isflipped = [False, False, False]

        # Extract prices for each pair, handling flipped pairs
        price1 = prices.get(symbol1 + symbol2) or prices.get(symbol2 + symbol1) or float(manual_value()[0].get())
        if prices.get(symbol1 + symbol2) is None:
            isflipped[0] = True

        price2 = prices.get(symbol2 + symbol3) or prices.get(symbol3 + symbol2) or float(manual_value()[1].get())
        if prices.get(symbol2 + symbol3) is None:
            isflipped[1] = True

        price3 = prices.get(symbol3 + symbol1) or prices.get(symbol1 + symbol3) or float(manual_value()[2].get())
        if prices.get(symbol3 + symbol1) is None:
            isflipped[2] = True

        intermediate_amount_1 = starting_amount * price1 if not isflipped[0] else starting_amount / price1
        intermediate_amount_2 = intermediate_amount_1 * price2 if not isflipped[1] else intermediate_amount_1 / price2
        final_amount = intermediate_amount_2 * price3 if not isflipped[2] else intermediate_amount_2 / price3

        return [intermediate_amount_1, intermediate_amount_2, final_amount, price1, price2, price3]
    except Exception as e:
        print(e)
        return [float(0), float(0), float(0), float(0), float(0), float(0)]


if __name__ == "__main__":
    pass
    # sample only
    starting_amount = 5
    symbol1 = 'USDT'
    symbol2 = 'BTC'
    symbol3 = 'BNB'

    result = calculate_profit(starting_amount, symbol1, symbol2, symbol3)
    print(result)
    # print(f"Starting with  :       {starting_amount:.10f} {symbol1:5}")
    # print(f"Trade {symbol1:9}:       {starting_amount:.20f} {symbol1:5} -> {result[0]:.20f} {symbol2:5}")
    # print(f"Trade {symbol2:9}:       {result[0]:.20f} {symbol2:5} -> {result[1]:.20f} {symbol3:5}")
    # print(f"Trade {symbol3:9}:       {result[1]:.20f} {symbol3:5} -> {result[2]:.20f}  {symbol1:5}")
    # print(f"Total profit   :       {result[2] - starting_amount:.20f} {symbol1:5}")
    # available_coins = get_binance_coins()

    # if available_coins:
    #     print("List of available coins on Binance:")
    #     for coin in available_coins:
    #         print(coin)
    # else:
    #     print("Failed to fetch the list of available coins.")
