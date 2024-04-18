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


	async def parse_html(self, html_data):
	
		parent = html_data.name
		data = {parent:[]}
		for x in html_data.children:
			if x.name and hasattr(x, "children"):
				data[parent].append(await self.parse_html(x))
				
			if not hasattr(x, "children"):
				if not data[parent]:
					data[parent].append({"text":x.getText()})
				else:
					data[parent].append({"text":x.getText()})
		return data
	
