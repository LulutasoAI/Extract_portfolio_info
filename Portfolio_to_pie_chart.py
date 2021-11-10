import numpy as np
import pandas_datareader as dt
import datetime
from matplotlib import pyplot as plt
import pickle_around
import portfolio_define

class Portfolio_to_Piechart():
    def __init__(self):
        pass

    def get_Yesterday_Today(self): 
        date_today=datetime.date.today() 
        duration_oneday=datetime.timedelta(days=1) 
        date_yesterday=date_today-duration_oneday  
        return date_today, date_yesterday

    def stock_search_to_prices(self,stock_symbol,start_date, end_date):
        df = dt.DataReader(stock_symbol,"yahoo", start_date, end_date)
        prices = df["Close"]
        return np.array(prices)

    def add_price_info_to_portfolio(self,portfolio):
        date_today, date_yesterday = self.get_Yesterday_Today()
        for stock_symbol in portfolio:
            price_latest = self.stock_search_to_prices(stock_symbol,date_yesterday,date_today)[-1]
            if type(portfolio[stock_symbol][-1]) == int:
                portfolio[stock_symbol].append(price_latest)
            else:
                portfolio[stock_symbol][-1] = price_latest
        return portfolio

    def process_data(self,up_to_date_portfolio,to_show=True):
        """
        It needs to be revised in the light of efficiency and readability.
        """
        labels = []
        sizes = []
        raw_amounts = []
        num_to_get_amount = 0
        num_to_get_price = 1
        total = 0
        for stock_symbol in up_to_date_portfolio:
            labels.append(stock_symbol)
            current_info = up_to_date_portfolio[stock_symbol]
            local_sum = current_info[num_to_get_amount] * current_info[num_to_get_price]
            raw_amounts.append(local_sum)
            total += local_sum
        if total == np.sum(raw_amounts): #This might be redundant but checking is important init.
            print("Variable check okay.")
        else:
            print(total,"vs",np.sum(raw_amounts))
            print("Something is wrong.")
        for amount in raw_amounts:
            sizes.append(amount/total)

       
        if to_show:
             #Pie chart generation process.
            
            plt.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            plt.axis('equal')
            plt.show()
        
        return total

    def process_for_chart(self,up_to_date_portfolio,to_show=True):
        """
        This function is for being called by another file, not for the internal use.
        """
        labels = []
        sizes = []
        raw_amounts = []
        num_to_get_amount = 0
        num_to_get_price = 1
        total = 0
        for stock_symbol in up_to_date_portfolio:
            labels.append(stock_symbol)
            current_info = up_to_date_portfolio[stock_symbol]
            local_sum = current_info[num_to_get_amount] * current_info[num_to_get_price]
            raw_amounts.append(local_sum)
            total += local_sum
        if total == np.sum(raw_amounts): #This might be redundant but checking is important init.
            print("Variable check okay.")
        else:
            print(total,"vs",np.sum(raw_amounts))
            print("Something is wrong.")
        for amount in raw_amounts:
            sizes.append(amount/total)

        return sizes, labels 


    def portfolio_to_piechart(self,portfolio):
        up_to_date_portfolio = self.add_price_info_to_portfolio(portfolio)
        total = self.process_data(up_to_date_portfolio)
        return up_to_date_portfolio, total

    def process_info_to_show(self,info_,total):
        date_today, date_yesterday = self.get_Yesterday_Today()
        USD_JPY_today = round(self.stock_search_to_prices("JPY=X",date_yesterday,date_today)[-1],2)

        for name in info_:
            print("{}'s current price : {}".format(name,round(info_[name][1],2)))
        print("Your current total asset : {} US Dollars.".format(int(total))) 
        print("Your current total asset in Yen : {} JPY".format(int(total*USD_JPY_today)))
        return int(total*USD_JPY_today)


if __name__ == "__main__":
    PP = Portfolio_to_Piechart()
    portfolio = portfolio_define.portfolio
    info_, total= PP.portfolio_to_piechart(portfolio)
    JPY_amount_that_day = PP.process_info_to_show(info_,total)
    pickle_around.add_data([info_,total,JPY_amount_that_day])