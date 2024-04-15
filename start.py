from stock_scraper.screener_scarper import ScreenerScraper
import asyncio

async def fetch_data():
    stock_scraper = ScreenerScraper()
    await stock_scraper.fetch_stock_data("RELIANCE")

if __name__  == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_data())
    
    
