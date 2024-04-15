from urllib.request import urlopen
from bs4 import BeautifulSoup

class WebScraper:


    def __init__(self):
        self.site_url = ""
    

    async def fetch_url_page(self, url):
        print(url)
        page = urlopen(url)
        html_bytes = page.read()
        html_string = html_bytes.decode("utf-8")
        return BeautifulSoup(html_string, "html.parser")

    
