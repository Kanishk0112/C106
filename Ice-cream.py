import plotly.express as px
import csv
import numpy as np
def Plotfig(datapath):
    with open(datapath) as csvfile:
        df=csv.DictReader(csvfile)
        fig=px.scatter(df,x="Temperature",y="Ice-cream")
        fig.show()
def Getdatasource(datapath):
    Temperature=[]
    Icecreamsales=[]
    with open(datapath) as csvfile:
        csvreader=csv.DictReader(csvfile)
        for row in csvreader:
            Temperature.append(float(row["Temperature"]))
            Icecreamsales.append(float(row["Ice-cream"]))
    return {"x": Temperature,"y":Icecreamsales}
def findcorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between Ice-cream and Temperature",correlation[0,1])
datapath="C:/Users/Hp/Desktop/White HAt Junior/PYTHON/C106/Ice-Cream.csv"
datasource=Getdatasource(datapath)
findcorrelation(datasource)
Plotfig(datapath)