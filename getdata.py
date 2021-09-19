#Vaibhav Turaga Twitter Data Project 

import twint
import matplotlib.pyplot as plot
from datetime import datetime
import matplotlib.animation as animation


def lastminute(keyword):

   #gets current time
    minute = int(int(datetime.today().strftime('%M'))-1)
    
    if minute == 0:
        minute = 59
    elif minute < 10:
        minute = "0" + str(minute) 

    oneminuteago = datetime.today().strftime('%Y-%m-%d %H:') + str(minute) + datetime.today().strftime(':%S')


    #searches for tweets about keyword and writes to file
    c = twint.Config()
    c.Search = keyword
    c.Since = oneminuteago
    c.Output = 'result.csv'
    c.Hide_output = True
    c.Count = True

    twint.run.Search(c)

    #searches file for number of lines
    count = 0
    with open("result.csv", encoding = 'utf8') as file:
        count = sum(1 for line in file)
    
    with open("result.csv", "w") as file:
        file.write('')

    return count, oneminuteago


x_vals = []
y_vals = []
data = {}

def animategraph(i):
    #adds new values to list of values to be graphed 
    count, oneminuteago = lastminute('dogecoin')
    x_vals.append(oneminuteago)
    y_vals.append(count)

    data.update({count: oneminuteago})

    #prints values that will be displayed on graph (time and number of tweets at the time)
    print(x_vals, y_vals)

    #plots data on graph
    plot.cla()
    
    plot.plot(x_vals, y_vals)


#updates graph
animate = animation.FuncAnimation(plot.gcf(), animategraph, interval = 0)
plot.show()



 
