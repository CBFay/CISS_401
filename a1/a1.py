import csv
import json

with open('GlobalLandTemperaturesByCity.csv') as csv_file:
    temperatures = csv.DictReader(csv_file)
    
    print('Temperatures in Stockholm in 1994:')
    stockholm_1994 = []
    for table in temperatures:
        if table['City'] == 'Stockholm' and table['dt'][:4] == '1994':
            stockholm_1994.append(table)
            print(table['dt'], ':', int(float(table['AverageTemperature'])))
            
    print()
    for month in stockholm_1994:
        print(json.dumps(month, indent=4))
        print()
    
    
