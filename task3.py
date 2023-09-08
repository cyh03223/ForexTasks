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

    # amount_cad is in CAD on start day
    amount_cad = 10000 * ratio
    # amount_usd is in USD on start day
    amount_usd = (10000 - amount_cad) * c.get_rate('CAD', 'USD', start_datetime)

    balance_arr = np.array([])
    for i in range(delta.days + 1):
        day = start_datetime + timedelta(days=i)
        balance_arr = np.insert(balance_arr, balance_arr.size, amount_cad + amount_usd * c.get_rate('USD', 'CAD', day))

    rng = pd.date_range(start_datetime, end_datetime, freq="D")
    ts = pd.Series(balance_arr, index=rng)
    return ts

# Simple Test Case:
# print(backward_test('2023/01/01', '2023/02/01', 'date'))