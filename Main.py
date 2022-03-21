from Stock_Ticker import StockTicker
from Stock_Caller import StockCaller
from Stock_Graph import StockGraph

stock_ticker_list = list()
stock_caller_list = list()

def get_stock_name():
    stock = input("Enter user stock name: ")
    return stock

def get_stock_list():
    flag = False
    while flag == False:
        local_st = StockTicker(get_stock_name())
        local_sc = StockCaller(local_st, start_date)
        local_sc.fetch()
        stock_ticker_list.append(local_st)
        stock_caller_list.append(local_sc)
        answer = input("would you like to obtain another stock: (y/n) ")
        if answer.lower() != "y":
            flag = True

def get_start_date():
    flag = False
    while not flag:
        try:
            start_date = int(input("Enter how many months of stock information you wish to obtain: "))
        except ValueError:
            print("Value must be an integer")
        else:
            flag = True
    return start_date

if __name__ == "__main__":
    start_date = get_start_date()
    get_stock_list()
    sg = StockGraph(stock_ticker_list)
    sg.graph()
