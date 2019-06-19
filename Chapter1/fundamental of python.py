from collections import namedtuple
price_str = '30.14, 29.58, 26.36, 32.56, 32.82'
price_str = price_str.replace(' ','')
#print(price_str)
price_array = list(price_str.split(','))
#print(price_array)
date_base = 20170118
date_array = [str(date_base + i) for i, _ in enumerate(price_array)]
#print(date_array)

#namedtuple
stock_namedtuple = namedtuple('stock',('date','price'))
stock_namedtuple_list = [stock_namedtuple(date, price) for date, price in zip(date_array, price_array)]
#print(stock_namedtuple_list)
#print('20170119 price: {}'.format(stock_namedtuple_list[1].price))

#dict
stock_dict = {date: price for date, price in zip(date_array, price_array)}
#print(stock_dict)

#OrderedDict
from collections import OrderedDict
stock_dict = OrderedDict((date, price) for date, price in zip(date_array, price_array))
#print(stock_dict)

def find_second_max(dict_array):
    stock_prices_sorted = sorted(zip(dict_array.values(), dict_array.keys()))
    return stock_prices_sorted[-2]

#print(find_second_max(stock_dict))

find_second_max_lambda = lambda dict_array: sorted(zip(dict_array.values(), dict_array.keys()))[-2]
#print(find_second_max_lambda(stock_dict))

def find_max_and_min (dict_array):
    stock_prices_sorted = sorted(zip(dict_array.values(), dict_array.keys()))
    return stock_prices_sorted[0], stock_prices_sorted[-1]
#print(find_max_and_min(stock_dict))

price_float_array = [float(price_str) for price_str in stock_dict.values()]
pp_array = [(price1, price2) for price1, price2 in zip(price_float_array[:-1], price_float_array[1:])]
#print(pp_array)

import functools
change_array = map(lambda pp: functools.reduce(lambda a, b: round((b - a) / a, 3), pp), pp_array)
change_array = list(change_array)
change_array.insert(0,0)
#print(change_array)
stock_namedtuple = namedtuple('stock', ('date', 'price', 'change'))
stock_dict = OrderedDict((date, stock_namedtuple(date, price, change)) for date, price, change in zip(date_array, price_array, change_array))
#print(stock_dict)

up_days = filter(lambda day: day.change > 0, stock_dict.values())
up_days = list(up_days)
#print(up_days)

#通用函数，筛选上涨或下跌的交易日，也可计算涨跌幅和
def filter_stock(stock_array_list, want_up = True, want_calc_sum = False):
    if not isinstance(stock_array_list, OrderedDict):
        raise TypeError('stock_array_dict must be OrderedDict!')
    filter_func = (lambda day: day.change > 0) if want_up else (lambda day: day.change < 0)
    want_days = filter(filter_func, stock_array_list.values())
    if not want_calc_sum:
        return want_days
    change_sum = 0.0
    for day in want_days:
        change_sum += day.change
    return change_sum

#partial function
from functools import partial
filter_stock_up_days = partial(filter_stock, want_up = True, want_calc_sum = False)
filter_stock_down_days = partial(filter_stock, want_up = False, want_calc_sum = False)
filter_stock_up_sums = partial(filter_stock, want_up = True, want_calc_sum = True)
filter_stock_down_sums = partial(filter_stock, want_up = False, want_calc_sum = True)

