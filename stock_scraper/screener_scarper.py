

from web_scraper.web_scraper import WebScraper
from bs4 import BeautifulSoup
scraper = WebScraper()


class ScreenerScraper(WebScraper):
    
    def __init__(self):
        super(WebScraper, self).__init__()
        self.site_url = "https://screener.in/"
        self.sections_to_scrape = {
            "main": [{"id":"top"}, {"id":"peers"}, {"id":"quarters"}, {"id":"profit-loss"}, {"id":"balance-sheet"}, 
            {"id":"cash-flow"}, {"id":"ratios"}, {"id":"shareholding"},
            {"id":"documents"}]
        }

    async def fetch_stock_data(self, stock_code):

        new_url = f"{self.site_url}company/{stock_code}/consolidated/"
        htmldata = await self.fetch_url_page(new_url)
        data = {}
        for k, v in self.sections_to_scrape.items():
            key_section = htmldata.find(k)
            if key_section:
                for sub_section in v:
                    x = await self.parse_html(key_section.find(id = sub_section['id']))
                    data[sub_section['id']] = x
        print(data)
       

        