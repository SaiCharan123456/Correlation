import plotly.express as px
import csv
import numpy as np
import pandas as pd

def plotFigure(data_path):
    df = pd.read_csv(data_path)
    df.sort_values(by=['Coffee in ml'])
    fig = px.scatter(df,x="Coffee in ml", y="sleep in hours", color="week")
    fig.show()

def getDataSource(data_path):
    Coffee_in_ml = []
    sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))

    return {"x" : Coffee_in_ml, "y": sleep_in_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Cups of Coffee vs Hours of Sleep :-  \n--->",correlation[0,1])

def setup():
    data_path  = "Correlation-P106/cups of coffee vs hours of sleep.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()
