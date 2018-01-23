# CB Fay
# Top Spotify Songs of 2017

import csv

lncount = 0
with open("data.csv") as f:
    readCSV = csv.reader(f, delimiter=',')
    for line in readCSV:
        print(line[:3])
        lncount += 1
        
        if lncount > 20:
            exit()
