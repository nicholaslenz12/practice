"""
Script that extracts data given in a csv file. Writes to file called REVEL.txt that on
each line has a variant with genomic coordinate and variation (relative to hg38).
"""
#------------------------------------------------------------------------------------------------
import csv # For csv file read/write
#------------------------------------------------------------------------------------------------
# Extracts from a file named out.csv on the desktop.
with open('/Users/nicholaslenz/Desktop/Internship/Data/out.csv', newline='') as csvfile: 
  Revel = open('/Users/nicholaslenz/Desktop/REVEL.txt', 'w') # Opens REVEL.txt for writing
  reader = csv.reader(csvfile, delimiter=' ', quotechar='|') # Creates csv reader
  for row in reader: # Iterates through each row in the reader
    new_list = row[0].split(",") # Elements of the row become elements of a list
    Revel.write(new_list[1])     # Writes the second element of the list to REVEL.txt
    Revel.write('\n')
  Revel.close()