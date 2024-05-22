from stock_scraper.screener_scarper import ScreenerScraper

class QuantitativeAnalyzer():

    def __init__(self, stock_name):

        self.screener_data = ScreenerScraper();
        self.stock_data = self.screener_data.fetch_stock_data(stock_name)



    def analyze_quarterly_results(self, quarter_table):



    def analyze_profit_loss_results(self, profit_loss_table):
        