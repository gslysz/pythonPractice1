import ReadPerfMonCsv as reader
import os

print("Starting...")
filename = "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\Arc250Hz1sEpochSpectrogram.csv"
filename = "\\\\taz\\Users\\Gord\\DataAnalysis\\2018\\2018_10_17 PerfMon LiveReview\\Arc250Hz4sEpochSpectrogram.csv"
graphFilename1 = reader.MakeChartForBytesUsed(filename, ylim=(0, 5e9))
graphFileName2 = reader.MakeChartThreads(filename)

# os.startfile(graphFilename1)
# os.startfile(graphFileName2)

print("Done!")
