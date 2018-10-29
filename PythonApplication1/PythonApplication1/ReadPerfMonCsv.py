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


def MakeChartForBytesUsed(filename, title = "Bytes", xlim=(0,1000), ylim=(0,5e9)):
    df = readCsvPandas(filename)

    yvals = df[df.columns[1]]
    indexVals= list(range(0, len(yvals), 1))
    xvals = [i * 0.5 for i in indexVals]   # points are taken every 30 sec.  So this time in minutes.

    #yvals=  yvals[0:1600]
    #xvals = xvals[0:1600]


    slope, intercept, r_value, p_value, std_err = linregress(xvals,yvals)
    slopeMb = slope / 1024 / 1024
    slopeMbHr = slopeMb * 60 
    slopeText = f'slope = {slopeMbHr:.3f} MB/hr'

    trendline = [slope * i + intercept for i in xvals]

    pngFileName= filename.replace(".csv","_bytes.png")

    plt.plot(xvals, yvals)
    plt.plot(xvals, trendline)

    ymax= ylim[1]
    plt.ylim(ylim[0], ylim[1])
    plt.xlim(xlim[0], xlim[1])

    plt.xlabel("time (min)")
    plt.ylabel("bytes")
    plt.title(title)
    plt.annotate(slopeText, xy=(0,ymax*0.9))
    plt.savefig(pngFileName)
    print(f'Saved graph to file: {pngFileName}')
    return pngFileName




def MakeChartThreads(filename, title = "Threads", xlim=(0,1000), ylim=(0,500)):
    df = readCsvPandas(filename)

    yvals = df[df.columns[2]]
    indexVals= list(range(0, len(yvals), 1))
    xvals = [i * 0.5 for i in indexVals]   # points are taken every 30 sec.  So this time in minutes.
    
    pngFileName= filename.replace(".csv","_threads.png")
    plt.plot(xvals, yvals)
    
    ymax= ylim[1]
    plt.ylim(ylim[0], ylim[1])
    plt.xlim(xlim[0], xlim[1])

    plt.xlabel("time (min)")
    plt.ylabel("threads")
    plt.title(title)
    plt.savefig(pngFileName)
    print(f'Saved graph to file: {pngFileName}')
    return pngFileName


#filename1= "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\ArcNoSpectrogram.csv"
#filename2= "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\ArcWithSpectrogram.csv"
#filename3= "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\ArcWithSpectrogram_15MinWindow.csv"
#filename4= "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\ArcWithSpectrogram_WindowCollapsed.csv"

#filenames= [filename1,filename2,filename3,filename4]

#for f in filenames:
#    MakeChartForBytesUsed(f)



