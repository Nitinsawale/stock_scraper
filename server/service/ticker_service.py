from server.modules.stock_scraper.stock_price_data_retriver import CandlePriceRetriever


def get_stock_data(ticker_name, time_period = "10y", time_interval="1d"):

    price_retriever = CandlePriceRetriever(ticker_name=ticker_name, ticker_type = "stock")
    df = price_retriever.fetch_data(time_period=time_period, time_interval=time_interval)
    return df.to_dict(orient="records")