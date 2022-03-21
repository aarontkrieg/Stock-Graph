from alpha_vantage.timeseries import TimeSeries
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from Stock_Ticker import StockTicker

file = "secwiki_tickers.csv"


class StockCaller:
    # Your key here
    def __init__(self, stock_ticker, start_date):
        self.st = stock_ticker
        self.start_date = start_date
        self.key = 'A0U3FIYS6RGQ5COI'

    def daterange(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

    def call_api(self):
        ts = TimeSeries(self.key)
        flag = False
        while not flag:
            try:
                api_return, meta = ts.get_daily(symbol=self.st.symbol, outputsize='full')
            except ValueError:
                self.st.symbol = str(input("Stock name does not exist, Please enter another stock name: "))
            else:
                flag = True
        return api_return

    def get_closing_prices(self, fetch_date, api_return):
        for single_date in self.daterange(fetch_date, date.today()):
            try:
                self.st.close_prices.append(float(api_return[str(single_date)]['4. close']))
            except KeyError:
                pass
            else:
                self.st.dates.append(str(single_date))

    def get_stock_name(self):
        handle = open(file)
        for line in handle:
            stock_info = line.split(',')
            if self.st.symbol == stock_info[0]:
                self.st.company_name = stock_info[1].replace('\"', '')
                return
        self.st.company_name = self.st.symbol

    def fetch(self):
        fetch_date = date.today() + relativedelta(months=-self.start_date)
        api_return = self.call_api()
        self.get_stock_name()
        self.get_closing_prices(fetch_date, api_return)
