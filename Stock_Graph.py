from matplotlib import pyplot as plt
import matplotlib.patches as mpatches
from Stock_Ticker import StockTicker

color_list = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'white']


class StockGraph:
    def __init__(self, stock_ticker_list):
        self.stlist = stock_ticker_list
        self.legend_list = list()
        self.fig = plt.figure(dpi=128, figsize=(10,6))

    def set_labels(self):
        _, ax = plt.subplots()
        ax.set_ylabel("Value in USD")
        ax.set_xlabel("Daily dates for stock prices")
        title = "Closing Prices for "
        for i in range(len(self.stlist)):
            if i != len(self.stlist) - 1:
                title = title + self.stlist[i].company_name + ", "
            else:
                title = title + "and " + self.stlist[i].company_name
        ax.set_title(title)
        return ax

    def set_stocks(self):
        for i in range(len(self.stlist)):
            plt.plot(self.stlist[i].dates, self.stlist[i].close_prices, c=color_list[i % 8])
            if self.stlist[i].symbol == self.stlist[i].company_name:
                self.legend_list.append(mpatches.Patch(color=color_list[i], label="(" + self.stlist[i].symbol + ")"))
            else:
                self.legend_list.append(mpatches.Patch(color=color_list[i], label=self.stlist[i].company_name + " (" + self.stlist[i].symbol + ")"))
        plt.legend(handles=self.legend_list)

    def graph(self):
        ax = self.set_labels()
        self.set_stocks()
        every_nth = 14
        for n, label in enumerate(ax.xaxis.get_ticklabels()):
            if n % every_nth != 0:
                label.set_visible(False)
        plt.show()



