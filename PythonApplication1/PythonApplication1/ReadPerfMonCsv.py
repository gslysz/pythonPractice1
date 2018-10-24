import numpy as np
import csv
import pandas
from scipy.stats import linregress
import matplotlib.pyplot as plt

def readCsvFile(filename):
    with open(filename, mode='r') as csvFile:
        reader = csv.reader(csvFile)
        lineCounter = 0
        for row in reader:
            if lineCounter==0:
                print(f'{",".join(row)}')
            else:
                print(f'{row[0]}\t{row[1]}')
            lineCounter+=1
        print(f'Processed {lineCounter} lines.')

def readCsvPandas(filename):
    df = pandas.read_csv(filename)
    return df
    
filename= "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\ArcNoSpectrogram.csv"
#filename= "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\ArcWithSpectrogram.csv"
#filename= "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\ArcWithSpectrogram_15MinWindow.csv"
#filename= "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\ArcWithSpectrogram_WindowCollapsed.csv"

df = readCsvPandas(filename)

yvals = df[df.columns[1]]
indexVals= list(range(0, len(yvals), 1))
xvals = [i * 0.5 for i in indexVals]   # points are taken every 30 sec.  So this time in minutes.

slope, intercept, r_value, p_value, std_err = linregress(xvals,yvals)
slopeMb = slope / 1024 / 1024
slopeMbHr = slopeMb * 60 
slopeText = f'slope = {slopeMbHr:.3f} MB/hr'

trendline = [slope * i + intercept for i in xvals]

pngFileName= filename.replace(".csv","_bytes.png")


plt.plot(xvals, yvals)
plt.plot(xvals, trendline)

ymax= 5e9

plt.ylim(0, 5e9)
plt.xlim(0, 1000)

plt.xlabel("time (min)")
plt.ylabel("num bytes")
plt.annotate(slopeText, xy=(0,ymax*0.9))

plt.savefig(pngFileName)

plt.show()



