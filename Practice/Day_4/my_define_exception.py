class NegativePriceException(Exception):
    def __init__(self):
        print('Price can\'t be negative')
        raise AttributeError

def calc_price(value):
    price = value * 1000
    if price < 0:
        raise NegativePriceException
    # return price
    print(price)

calc_price(4)
calc_price(-1)