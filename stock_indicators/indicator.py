from abc import ABC
import pandas as pd
import pandas_ta as pta
from numpy import nan
def decorator_timer(some_function):
    from time import time

    def wrapper(*args, **kwargs):
        t1 = time()
        result = some_function(*args, **kwargs)
        end = time()-t1
        print(end)
        return result
    return wrapper



class TickerIndicator(ABC):
    pass



class TrueRange:


    def __init__(self, data_df, timeframe):
        self.data_df = data_df
        self.timeframe = timeframe 


    def true_range_calculator(self, row, previous_row):
        return max([(row['high'] - row['low']),  abs(row['high'] - previous_row['close']), abs(row['low'] - previous_row['close'])])
    

    @decorator_timer
    def calculate_indicator_values(self):

        self.data_df['tr1'] = self.data_df['high'] - self.data_df['low']
        self.data_df['tr2'] = (self.data_df['high'] - self.data_df['close'].shift()).abs()
        self.data_df['tr3'] = (self.data_df['low'] - self.data_df['close'].shift()).abs()
        self.data_df['true_range'] = self.data_df[['tr1', 'tr2', 'tr3']].max(axis = 1).fillna(0)
        return self.data_df


class AverageTrueRange:

    def __init__(self, data_df, timeframe):
        self.data_df = data_df
        self.timeframe = timeframe 


    @decorator_timer
    def calculate_indicator_values(self, window):

        true_range_object  = TrueRange(self.data_df, self.timeframe)
        self.data_df = true_range_object.calculate_indicator_values()
        self.data_df.iloc[:1] = nan
        self.data_df['average_true_range'] =  self.data_df['true_range'].iloc[1:].ewm(alpha = 1 / window,  min_periods = window).mean()
        return self.data_df

if __name__ == "__main__":
   
    data = pd.read_excel("./^NSEI_1d.xlsx")
    tr = AverageTrueRange(data, '1d')
    df = tr.calculate_indicator_values(14)
    df['data_to_test'] = pta.atr(data['high'], data['low'], data['close'], length=14)
    df.to_excel('test.xlsx', index = False)
    import pdb;pdb.set_trace()