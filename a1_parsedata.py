# CB Fay
# Top Spotify Songs of 2017

import csv
import json

lncount = 0
with open("data.csv") as f:
    readCSV = csv.reader(f, delimiter=',')
    
    # Print Formatted Fields
    for line in readCSV:
        print(line[:3])
        lncount += 1
 
        if lncount > 20:
            print()
            break
            
            
    # Print JSON format
    data = list(readCSV)
    print(json.dumps([line[:3] for line in data[:20]]))
