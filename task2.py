import numpy as np
import pandas as pd

def get_golden_ratio(date, curve_type):
    year = date[0:4]
    month = date[0:7]
    year_ts = pd.Series(np.random.random_sample(), index=pd.date_range(year, periods=1000))
    month_ts = pd.Series(np.random.random_sample(), index=pd.date_range(month, periods=1000))
    date_ts = pd.Series(np.random.random_sample(), index=pd.date_range(date, periods=1000))
    if curve_type == "year":
        return year_ts[date]
    elif curve_type == "month":
        return month_ts[date]
    elif curve_type == "date":
        return date_ts[date]
    else:
        print("Such curve type is not existed.")

# Simple Test Case:
# print(get_golden_ratio("2021/02/01", "date"))