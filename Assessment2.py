import datetime 
import portfolio_define 
import numpy as np
from matplotlib import pyplot as plt
import pandas_datareader as dt


class Portfolio_Assessment():
    def __init__(self):
        self.portfolio = portfolio_define.portfolio
        self.duration = 30
        self.start = "2019-01-01"
        self.end = datetime.date.today()
    
    #Utils 
    def JPY_X_rate_N_date(self,start_date, end_date):
        FX_info = {}
        JPYX_Rate = dt.DataReader("JPY=X","yahoo", start_date, end_date)
        for i in range(len(JPYX_Rate)):
            FX_info["{}".format(JPYX_Rate.index[i])] = JPYX_Rate["Close"][i]  
        return FX_info

    def stock_search_to_Date_Prices(self,stock_symbol,start_date, end_date):
        df = dt.DataReader(stock_symbol,"yahoo", start_date, end_date)
        return df.index,np.array(df["Close"])

    def main(self,to_show=True):
        #date USD JPY rate 
        FX_info = self.JPY_X_rate_N_date(self.start, self.end)


        data = {}
        for i, name in enumerate(self.portfolio):
            data[name] = [self.stock_search_to_Date_Prices(name,self.start,self.end)]

        X = []
        Y = []
        for i in range(self.duration):
            USD_total = 0
            for name in self.portfolio:
                if i== 0:
                    date = data[name][0][0][-(i+1):]
                    price = data[name][0][1][-(i+1):]
                else:
                    date = data[name][0][0][-(i+1):-(i)]
                    price = data[name][0][1][-(i+1):-(i)]
                USD_total += price*self.portfolio[name][0]
            try:
                temp = round(FX_info[str(date[0])],2)
                JPY = USD_total * round(FX_info[str(date[0])],2)
            except:
                JPY = USD_total * temp
            X.append(date[0])
            Y.append(JPY)
        if to_show:
            plt.plot(X,Y)
            plt.tight_layout()
            plt.xlabel("Date")
            plt.ylabel("JPY")
            plt.title("Your Portfolio Performance")
            plt.show()
        else:
            return X,Y
if __name__ == "__main__":
    PA = Portfolio_Assessment()
    PA.main()