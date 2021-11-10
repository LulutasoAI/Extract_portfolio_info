from Assessment2 import Portfolio_Assessment
from Portfolio_to_pie_chart import Portfolio_to_Piechart
from PieandPerformance import Pie_chart_and_History_graph

import sys
if __name__ == "__main__":
    max_orders = 3
    message = """
                0 for creating pie chart based on your portfolio.
                1 for creating visualised graph based on the former performance of your portfolio.
                2 for creating both at once. 
                """
    try:
        order = int(sys.argv[1]) 
    except:
        print(message)
        sys.exit()
    if order == 0:
        Portfolio_to_Piechart().main()
    elif order == 1:
        Portfolio_Assessment().main()
    elif order == 2:
        Pie_chart_and_History_graph().main()
    else:
        err_message = "Your order '{}' is, therefore, not acceptable. choose between {} and {}".format(sys.argv[1],0,max_orders-1)
        print(message)
        print(err_message)
        
        sys.exit()
    
