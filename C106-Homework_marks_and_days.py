import csv
import plotly.express as px
import numpy as np
import pandas as pd

def getDataSource(dataPath):
     marksPercent = []
     daysAttended = []

     with open(dataPath) as csvFile:
          csvReader = csv.DictReader(csvFile)
          for row in csvReader:
              marksPercent.append(float(row["Marks In Percentage"]))
              daysAttended.append(float(row["Days Present"]))

          return {"x": marksPercent, "y": daysAttended}

def findCorrelation(dataSource):
     cr = np.corrcoef(dataSource["x"], dataSource["y"])

     print("Correlation of marks and days is = " + str(cr))

def graphPlot():
     df = pd.read_csv("Student Marks vs Days Present.csv")
     fig = px.scatter(df, x = "Marks In Percentage", y = "Days Present", color="Roll No")
     fig.show()

def setup():
     dataPath = "Student Marks vs Days Present.csv"

     dataSource = getDataSource(dataPath)
     findCorrelation(dataSource)
     graphPlot()

setup()
     
