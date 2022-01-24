import plotly.express as px
import csv
import numpy as np

def plotfig (data_path):
    with open (data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x='Temperature',y='Ice-cream Sales')
        fig.show()

    

def getDataSource (data_path):
    icecreamsales = []
    temperature = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            icecreamsales.append(float(row['Ice-cream Sales']))
            temperature.append(float(row['Temperature']))
    return {'x':icecreamsales,'y':temperature}

def findCorrelation (datasource):
    correlation = np.corrcoef(datasource['x'],datasource['y'])
    print('correlation between Temperature and Icecream sale is : ',correlation[0,1])

def setup ():
    data_path = 'Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv'
    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotfig(data_path)

setup()

