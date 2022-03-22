import plotly.express as px
import csv
import numpy as np
def Plotfig(datapath):
    with open(datapath) as csvfile:
        df=csv.DictReader(csvfile)
        fig=px.scatter(df,x="Coffee",y="sleep")
        fig.show()
def Getdatasource(datapath):
    Coffee=[]
    sleep=[]
    with open(datapath) as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            Coffee.append(float(row["Coffee"]))
            sleep.append(float(row["sleep"]))
    return {"x": Coffee,"y":sleep}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between Coffee and sleep",correlation[0,1])
datapath="C:/Users/Hp/Desktop/White HAt Junior/PYTHON/C106/coffee.csv"
datasource=Getdatasource(datapath)
findcorrelation(datasource)
Plotfig(datapath)