# #!/usr/bin/env python
# #chp3.py
# #Ciera Martinez
#
# #arguments
# #1. a file that containts text to search
#
# import re
# import sys
#
# #This sets up output file
# orig_stdout = sys.stdout
# data = open("./data/pyOutputs/chapterPosition.txt", 'w')
# sys.stdout = data
#
# #prints the headers of columns
# print 'chapter\tposition'
#
# sampleText = open(sys.argv[1]) #file that contains text
# sampleRead = sampleText.read() #Makes one item string
#
# #for everytime the chapter tag is found, it will print tag and position
# for m in re.finditer("<ch><\d\d>", sampleRead):
# 	print m.group(0), "\t", m.start()
#
# #Outputs print
# sys.stdout = orig_stdout
#
# sampleText.close()
# data.close()
#
#
#
from collections import OrderedDict

document = [['A', 'B'], ['C', 'B'], ['A', 'B', 'C', 'D']]
names = ['A', 'B', 'C', 'D']

occurrences = OrderedDict((name, OrderedDict((name, 0) for name in names)) for name in names)

# Find the co-occurrences:
for l in document:
    for i in range(len(l)):
        for item in l[:i] + l[i + 1:]:
            occurrences[l[i]][item] += 1

# Print the matrix:
print(' ', ' '.join(occurrences.keys()))
for name, values in occurrences.items():
    print(name, ' '.join(str(i) for i in values.values()))
