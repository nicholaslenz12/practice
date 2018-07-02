fileR = open('/Users/nicholaslenz/Desktop/VEPScores.txt', 'r')
fileW = open('/Users/nicholaslenz/Desktop/VEPScoresOut.txt', 'w')
for line in fileR:
	new_list = line.split('\t')
	fileW.write(new_list[0] + " ")
	for item in new_list:
		newer_list = item.split(",")
		if ( "benign" in newer_list or "likely_benign" in newer_list or \
		"uncertain_significance" in newer_list or "pathogenic" in newer_list or \
		"likely_pathogenic" in newer_list ):
			if ( "benign" in newer_list ):
				fileW.write("benign")
			elif( "likely_benign" in newer_list):
				fileW.write("likely_benign")
			elif( "uncertain_significance" in newer_list ):
				fileW.write("uncertain_significance")
			elif( "pathogenic" in newer_list ):
				fileW.write("pathogenic")
			elif( "likely_pathogenic" in newer_list ):
				fileW.write("likely_pathogenic")
	fileW.write('\n')
fileR.close()
fileW.close()