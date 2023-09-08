import pandas as pd
from datetime import timedelta
from forex_python.converter import CurrencyRates

def get_avg_rate(start_date, end_date, forex_type):
    c = CurrencyRates()
    cur1 = forex_type[0:3]
    cur2 = forex_type[4:7]

    start_datetime = pd.to_datetime(start_date, format='%Y/%m/%d')
    end_datetime = pd.to_datetime(end_date, format='%Y/%m/%d')
    delta = end_datetime - start_datetime

    sum = 0

    for i in range(delta.days + 1):
        day = start_datetime + timedelta(days=i)
        print(c.get_rate(cur1, cur2, day))
        sum += c.get_rate(cur1, cur2, day)

    return sum / (delta.days + 1)

# Simple Test Case:
# print(get_avg_rate('2023/01/01', '2023/02/01', 'USD/CAD'))