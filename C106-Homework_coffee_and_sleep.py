import csv
import plotly.express as px
import numpy as np
import pandas as pd

def getDataSource(dataPath):
     coffeeMl = []
     sleepHr = []

     with open(dataPath) as csvFile:
          csvReader = csv.DictReader(csvFile)
          for row in csvReader:
              coffeeMl.append(float(row["Coffee in ml"]))
              sleepHr.append(float(row["sleep in hours"]))

          return {"x": coffeeMl, "y": sleepHr}

def findCorrelation(dataSource):
     cr = np.corrcoef(dataSource["x"], dataSource["y"])

     print("Corellation b/w Coffee and sleep is = " + str(cr))

def graphPlot():
     df = pd.read_csv("cups of coffee vs hours of sleep.csv")
     fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours", color="week")
     fig.show()

def setup():
     dataPath = "cups of coffee vs hours of sleep.csv"

     dataSource = getDataSource(dataPath)
     findCorrelation(dataSource)
     graphPlot()

setup()
