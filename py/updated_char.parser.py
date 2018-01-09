#!/usr/bin/env python
#char.parser.py

import re
import sys
import pandas as pd

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
		current_pos=next_pos
		
df_char_count = df_chapters.groupby(['chapter', 'term']).size().reset_index(name='counts')
df_chapters.to_csv('samantha_characters_position_chapters.csv')
df_char_count.to_csv('samantha_characters_counts_chapters.csv')


sampleText.close()
listOfTerms.close()
