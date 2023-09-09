import task2
import numpy as np
import pandas as pd
from datetime import timedelta
from forex_python.converter import CurrencyRates

# Output the daily balance as time series in CAD
def backward_test(start_date, end_date, get_ratio):
    # Suppose ratio is the ratio of CAD compared with USD
    c = CurrencyRates()
    ratio = task2.get_golden_ratio(start_date, get_ratio)
    start_datetime = pd.to_datetime(start_date, format='%Y/%m/%d')
    end_datetime = pd.to_datetime(end_date, format='%Y/%m/%d')
    delta = end_datetime - start_datetime

    balance_arr = np.array([10000])
    for i in range(delta.days):
        pre_day = start_datetime + timedelta(days=i)
        cur_day = start_datetime + timedelta(days=(i+1))
        cur_cad = balance_arr[balance_arr.size - 1] * ratio
        cur_usd = balance_arr[balance_arr.size - 1] * (1 - ratio) * c.get_rate('CAD', 'USD', pre_day) * c.get_rate('USD', 'CAD', cur_day)
        cur_total = cur_cad + cur_usd
        balance_arr = np.insert(balance_arr, balance_arr.size, cur_total)
        ratio = task2.get_golden_ratio(cur_day.strftime("%Y/%m/%d"), get_ratio)

    rng = pd.date_range(start_datetime, end_datetime, freq="D")
    ts = pd.Series(balance_arr, index=rng)
    return ts

# Simple Test Case:
# print(backward_test('2016/01/01', '2016/02/01', 'date'))