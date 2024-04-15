

from web_scraper import WebScraper

scraper = WebScraper()


class ScreenerScraper(WebScraper):
    
    def __init__(self):
        super(WebScraper, self).__init__()
        self.site_url = "https://screener.in/"

    async def fetch_stock_data(self, stock_code):

        new_url = f"{self.site_url}company/{stock_code}/consolidated/"
        htmldata = await self.fetch_url_page(new_url)
        data_in_dictionary = await self.scrape_data_from_html(htmldata)


    async def scrape_data_from_html(self, html_data):
        main_section  = html_data.find("main")
        if main_section:
            top_section_details = await self.parse_top_section(main_section.find(id = "top"))

    

    async def parse_top_section(self, section_html):

        data = {}
        data['security_name'] = section_html.find("h1").getText()
        data['security_price'] = section_html.find("span").getText()
        data['links'] = {}
        security_related_links = section_html.find(class_="company-links").findAll("a")
        for link in security_related_links:
            data['links'][link.getText()] = link['href']
        
        company_info = section_html.find(class_ = "company-info")
        company_ratios = company_info.find(class_="company-ratios")
        company_profile = section_html.find(class_ = "company-profile")

        data['company_profile'] = {}
        texts  = company_profile.findAll("p")
        titles = company_profile.findAll(class_='title')
        for index, title in enumerate(titles):
            data['company_profile'][title.getText()] = texts[index].getText()
        
        data['company_ratios'] = {}
        all_ratios = company_ratios.find(id = "top-ratios").findAll("li")
        for ratio in all_ratios:
            data['company_ratios'][ratio.find(class_='name').getText()] = ratio.find(class_="value").getText()
        
        return data



