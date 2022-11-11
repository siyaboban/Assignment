#mporting libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#creating a dataframe to read the excel file using pandas and to print
df = pd.read_excel("C:/Users/baxba/Documents/Population Growth%.xlsx")
print(df)

#function to plot line graph
def linegraph(): 
    plt.figure()
    #plotting line graph
    plt.plot(df["Year"],df["China"],label= "China")
    plt.plot(df["Year"],df["Mexico"],label= "Mexico")
    plt.plot(df["Year"],df["New Zealand"],label= "New Zealand")
    plt.plot(df["Year"],df["United Kingdom"],label= "United Kingdom")
    #plotting x-label and y-label
    plt.xlabel("Year")
    plt.ylabel("Population Growth (annual%)")
    plt.xlim(1998,2022)
    plt.ylim(0,3.0)
    plt.legend()
    #setting the title
    plt.title("Population Growth",fontsize=18)
    #saving the figure into a file
    plt.savefig("lineplot.png", bbox_inches="tight")
    #displaying the function
    plt.show()
#calling the function
linegraph()

#function to plot bargraph
def bargraph():
    plt.figure()
    #plotting the bar graph
    plt.bar(df["Year"]+0.00,df["China"],label="China", width=1, color= "blue")
    plt.bar(df["Year"]+1.0,df["Mexico"],label="Mexico", width=1, color= "green")
    plt.bar(df["Year"]+2.0,df["New Zealand"],label="New Zealand", width=1, color="red")
    plt.bar(df["Year"]+3.0,df["United Kingdom"],label="United Kingdom", width=1, color="pink")
    #plotting x-label and y-label
    plt.xlabel("Year")
    plt.ylabel("Population Growth(Annual%)")
    #add the legend
    plt.legend()
    #setting the title
    plt.title ("Population Growth",fontsize=18)
    plt.savefig("lineplot.png", bbox_inches="tight")
    #displaying the function
    plt.show()
#calling the function
bargraph()

#imported new data from data world to form pie chart
Countries=["United Kingdom", "United States","Japan", "Brazil","Germany"]
tp=np.array([67326569,331893745,125681593,213993441,83129285])

def piechart ():
    #plotting pie chart
    plt.figure()
    plt.pie(tp,labels=Countries,autopct='%.2f%%')
    #setting title
    plt.title ("Total Population in 2021",fontsize=18)
    #add the legend
    plt.legend(loc='upper right',fontsize=10)
    plt.savefig("lineplot.png", bbox_inches="tight")
    #displaying the function
    plt.show()
#calling the function
piechart()
