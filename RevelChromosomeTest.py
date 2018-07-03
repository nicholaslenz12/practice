"""
Script that converts the notation given by the REVEL website for a genetic variant to genomic
coordinate notation (for hg38).
"""
#------------------------------------------------------------------------------------------------
import csv # For csv file read/write
#------------------------------------------------------------------------------------------------
# Opens the csv file with awful name revel_chrom_01_00035142-09793461 provided by the REVEL website for reading
with open('/Users/nicholaslenz/Desktop/revel_chrom_01_00035142-09793461.csv', newline='') as csvfile:
	RevelTest = open('/Users/nicholaslenz/Desktop/REVELTest.txt', 'w') # Opens REVELtest.txt for writing
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|') # Creates a reader
	for row in reader: # Iterates through each row in the csv file
		# The following lines in this code block formats the variant into genomic coordinate notation
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
