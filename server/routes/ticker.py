from fastapi import APIRouter
from server.service.ticker_service import get_stock_data
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get('/ticker-data/{ticker_name}/{time_period}/{time_interval}')
def get_ticker_data(ticker_name, time_period, time_interval):

    data =get_stock_data(ticker_name = ticker_name, time_period= time_period, time_interval=time_interval)
    return data
