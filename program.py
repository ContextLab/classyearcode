import csv
with open('temp.csv', 'rU') as file:
	csvfile = csv.reader(file, delimiter=",")
	for row in csvfile:
		date = row[1]
		date = date.split("/")
		date = [date[0], date[2]]
		if int(date[0]) > 6:
			date[1] = int(date[1]) + 1
		sy = int(date[1])
		cl = int(row[2])
		year = 4 - (cl - sy)
		print row[0] + "," + str(year)
