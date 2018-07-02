import csv
with open('/Users/nicholaslenz/Desktop/revel_chrom_01_00035142-09793461.csv', newline='') as csvfile:
	RevelTest = open('/Users/nicholaslenz/Desktop/REVELTest.txt', 'w')
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in reader:
		new_list = row[0].split(",")
		new_string = ""
		new_string += "chr"
		new_string += new_list[0]
		new_string += ":g."
		new_string += new_list[1]
		new_string += ":"
		new_string += new_list[3]
		new_string += ">"
		new_string += new_list[2]
		new_string += "\n"
		RevelTest.write(new_string)
	RevelTest.close()
