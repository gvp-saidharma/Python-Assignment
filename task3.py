# 3- Replace the word into file and count.

# # Read in the file
# with open('file.txt', 'r') as file :
#   filedata = file.read()

# # Replace the target string
# filedata = filedata.replace('ram', 'abcd')

# # Write the file out again
# with open('file.txt', 'w') as file:
#   file.write(filedata)


#input file
fin = open("../data.txt", "rt")

#output file to write the result to
fout = open("../out.txt", "wt")

#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('pyton', 'python'))

#close input and output files
fin.close()
fout.close()