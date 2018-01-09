#!/usr/bin/env python
#char.parser.py
#Ciera Martinez

#This script takes in two arguments
#1. text file (sampleText)
#2. List of terms to seach text file (listOfTerms)
# and then prints all terms and their postion in text file
# outputs results into ./data directory "charList.txt"

#sample command to run (for infinite jest project)
#python py/char.parser.py data/bookText/David-Foster-Wallace-Infinite-Jest-v2.0.txt data/character/characters.mod.txt

import re
import sys
import pandas as pd
import io


sampleText = io.open(sys.argv[1], mode='r', encoding='utf-8') #file that contains text
listOfTerms = open(sys.argv[2]) #file that contains terms to search for

sampleRead = sampleText.read() #Makes one item string
termRead = listOfTerms.read()
termSplit = termRead.splitlines() #split by new line
df_chapters = pd.DataFrame(columns=['chapter', 'term', 'position'])


current_pos = 0
for term in termSplit:
	for match in re.finditer("<ch><\d\d>", sampleRead):
		next_pos=match.end()
		current_text = sampleRead[current_pos:next_pos]
		for m in re.finditer(term, current_text):
			if m:
				print('position',match.group(0),m.group(0), m.span())
				df_chapters.loc[len(df_chapters)] = [match.group(0),m.group(0), m.span()]

			else:
				pass
				# return null, null
		current_pos=next_pos
print(df_chapters)
df_char_count = df_chapters.groupby(['chapter', 'term']).size().reset_index(name='counts')
print(df_char_count)
df_chapters.to_csv('samantha_characters_position_chapters.csv')
df_char_count.to_csv('samantha_characters_counts_chapters.csv')
# print(dict_chapters)
#Outputs print
# sys.stdout = orig_stdout

sampleText.close()
listOfTerms.close()
# data.close()
