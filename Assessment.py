import datetime 
import os 
from get_price_historyup_graded import Get_history
import numpy as np
from matplotlib import pyplot as plt

GH = Get_history()
portfolio = GH.portfolio
duration = 30
start = "2019-01-01"
end = datetime.date.today()

#date USD JPY rate 
FX_info = GH.JPY_X_rate_N_date(start, end)

data = {}
for i, name in enumerate(portfolio):
    data[name] = [GH.stock_search_to_Date_Prices(name,start,end)]

#print(data)
X = []
Y = []
for i in range(duration):
    USD_total = 0
    for name in portfolio:
        if i== 0:
            date = data[name][0][0][-(i+1):]
            price = data[name][0][1][-(i+1):]
        else:
            date = data[name][0][0][-(i+1):-(i)]
            price = data[name][0][1][-(i+1):-(i)]
        USD_total += price*portfolio[name][0]
        #print(price,"price")
    try:
        temp = round(FX_info[str(date[0])],2)
        JPY = USD_total * round(FX_info[str(date[0])],2)
    except:
        JPY = USD_total * temp
    #print(date[0],print(USD_total),"result")
    X.append(date[0])
    Y.append(JPY)
plt.plot(X,Y)
plt.xlabel("Date")
plt.ylabel("JPY")
plt.title("Your Portfolio Performance")
plt.show()