import os
import pandas as pd
import yfinance as yf
import logging
from constants import CHART_DATA_STORAGE_LOCATION

logger = logging.basicConfig(level=logging.INFO)

class CandlePriceRetriever:

    def __init__(self, ticker_name, ticker_type="stock"):
        self.ticker_name = ticker_name
        self.ticker_type = ticker_type
        if not os.path.exists(CHART_DATA_STORAGE_LOCATION):
            os.mkdir(CHART_DATA_STORAGE_LOCATION)


    def fetch_data(self,time_period, time_interval):

        file_location = CHART_DATA_STORAGE_LOCATION + f"{self.ticker_name}_{time_interval}.xlsx"
        
        if os.path.exists(file_location):
            logging.info(f"reading from local")
            return pd.read_excel(file_location)
        
        data =  self.fetch_data_from_yahoo_finanance(time_period, time_interval)
        columns = data.columns.tolist()
        columns = {x:x.lower() for x in columns}
        data.rename(columns =columns, inplace=True)
        data['date'] = data['date'].apply(lambda x: pd.to_datetime(x).date())
        data.to_excel(file_location, index = False)
        return data

    def fetch_data_from_yahoo_finanance(self,time_period, time_interval):
        logging.info(f"fetching {self.ticker_type} for {time_period} and {time_interval} interval from yahoo finance")
        ticker_to_fetch = f"{self.ticker_name}.NS"
        if self.ticker_type == 'index':
            ticker_to_fetch = self.ticker_name
        
        data = yf.Ticker(ticker_to_fetch)
        df = data.history(time_period, interval = time_interval)
        return df.reset_index()
        



if  __name__ == "__main__":
    obj = CandlePriceRetriever("^NSEI", ticker_type="index")
    obj.fetch_data("10y", "1d")