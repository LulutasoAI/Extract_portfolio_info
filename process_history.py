import pickle_around
from matplotlib import pyplot as plt
import datetime 
import matplotlib
if __name__ == "__main__":
    data_loaded = pickle_around.load_object()
    historical_assets_JPY = []
    Data_date = []
    for date in data_loaded:
        
        print("The data of ",date)
        extracted = data_loaded[date]
        #print(type(extracted[0]))
        USD_amount = extracted[1]
        JPY_amount = extracted[2]
        Data_date.append(datetime.datetime.strptime(date,"%Y%m%d"))
        print(extracted[0]," Stock prices of that day.")
        print("The total asset in USD : ",USD_amount,"USD")
        print("The total asset in JPY : ",JPY_amount,"JPY")
        print("USDJPY rate at that day : ",(int(JPY_amount)/round(USD_amount,2)))
        historical_assets_JPY.append(int(JPY_amount))
    #print(type(Data_date))
    Date_data = matplotlib.dates.date2num(Data_date)
    plt.plot(Data_date,historical_assets_JPY)
    plt.xlabel("Date")
    plt.ylabel("Asset in JPY")
    plt.tight_layout()
    plt.title("Your Asset history in JPY")
    plt.show()