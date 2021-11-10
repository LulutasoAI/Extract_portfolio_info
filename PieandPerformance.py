from Assessment2 import Portfolio_Assessment
from Portfolio_to_pie_chart import Portfolio_to_Piechart
import portfolio_define
from matplotlib import pyplot as plt

class Pie_chart_and_History_graph():
    
    def __init__(self):
        pass

    def main(self):
        PA = Portfolio_Assessment()
        PP = Portfolio_to_Piechart()

        #Pie chart process
        portfolio = portfolio_define.portfolio
        up_to_date_portfolio = PP.add_price_info_to_portfolio(portfolio)
        sizes,labels = PP.process_for_chart(up_to_date_portfolio)
        fig = plt.figure()
        pie = fig.add_subplot(1,2,1)
        pie.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
        pie.axis('equal')

        X,Y = PA.main(False)
        history = fig.add_subplot(1,2,2)
        history.plot(X,Y)
        history.set_xlabel("Date")
        history.set_ylabel("JPY")
        history.set_title("Your Portfolio Performance")
        fig.tight_layout()
        fig.show() #It didnt work so I will execute plt.show()below.
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    PH = Pie_chart_and_History_graph()
    PH.main()
