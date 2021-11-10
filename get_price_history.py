from Portfolio_to_pie_chart import Portfolio_to_Piechart
import datetime
import portfolio_define
from matplotlib import pyplot as plt
class Get_history():
    def __init__(self):
        self.portfolio = portfolio_define.portfolio
        self.duration = 30 #days 
        self.PP = Portfolio_to_Piechart()
        self.date, self.date_yesterday,self.duration_oneday = self.get_date_variables()
        self.fixed_today = self.date
        print(type(self.date),"date type at init")
        self.stock_search_to_prices = self.PP.stock_search_to_prices #name, start, end
        pass 
    
    def main(self):
        """
        1. get prices based on the portfolio data:
            info = {name:prices}
        2. 
        """
        result = {}
        for i in range(self.duration):
            portfolio_with_info_added = self.add_price_info_to_portfolio_for_any_date(self.portfolio,self.date)
            total = self.process_data_wrap(portfolio_with_info_added)
            total = self.USD_to_Yen(total,self.date)
            result[self.date] = total
            dummy, self.date = self.one_day_back(self.date)
        X,Y = self.process_info_to_x_y(result)
        self.plotter(X,Y)



    def plotter(self,X,Y):
        plt.plot(X,Y)
        plt.xlabel("Date")
        plt.ylabel("Asset in JPY")
        plt.tight_layout()
        plt.title("Your Asset history in JPY")
        plt.show()

    def process_info_to_x_y(self,info_):
        X = []
        Y = []
        for info_a_day in info_:
            X.append(info_a_day)
            Y.append(info_[info_a_day])
        return X,Y

    def get_date_variables(self):
        #1
        date_today=datetime.date.today() 
        duration_oneday=datetime.timedelta(days=1) 
        date_yesterday=date_today-duration_oneday  
        return date_today, date_yesterday, duration_oneday

    def one_day_back(self,day):
        #4
        duration_oneday=datetime.timedelta(days=1)
        print(type(duration_oneday),type(day))
        print(day,duration_oneday)
        one_day_before = day - duration_oneday
        return day, one_day_before

    def add_price_info_to_portfolio_for_any_date(self,portfolio,the_day):
        #2
        """
        return up_to_date_portfolio
        """
        print(type(the_day),"type of the_day at add_price")
        #date_today, date_yesterday = self.get_Yesterday_Today()
        end,start = self.one_day_back(the_day)
        for stock_symbol in portfolio:
            price_latest = self.stock_search_to_prices(stock_symbol,start,end)[-1]
            if type(portfolio[stock_symbol][-1]) == int:
                portfolio[stock_symbol].append(price_latest)
            else:
                portfolio[stock_symbol][-1] = price_latest
        return portfolio

    def process_data_wrap(self,up_to_date_portfolio):
        #3
        total = self.PP.process_data(up_to_date_portfolio,False)
        return total


    def USD_to_Yen(self,total,the_date):
        end,start = self.one_day_back(the_date)
        USD_JPY_today = round(self.stock_search_to_prices("JPY=X",start,end)[-1],2)
        return int(total*USD_JPY_today)



if __name__ == "__main__":
    get_history = Get_history()
    get_history.main()