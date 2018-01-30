import csv
import json

with open("chocolate.csv") as file:
	reader = list(csv.reader(file, delimiter=','))
    
	keys = reader[0]
	data = reader[1:]
	
	entries = []
	
	for values in data:
		entries.append(dict(zip(keys, values)))
		
	print('The worst 100 chocolate bars:')
	for bar in entries[-100:]:
		print(bar['Company'], bar['Bar Name'])
	
	
	
	with open("badchocolate.json", "w") as file2:
		json.dump(entries[-100:], file2)
