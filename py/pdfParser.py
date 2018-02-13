import re
import sys
import textract
import PyPDF2
import pandas as pd

pdf = PyPDF2.PdfFileReader(open('David-Foster-Wallace-Infinite-Jest-v2.0.pdf', "rb"))

num_of_pages = pdf.getNumPages()
df_text_page = pd.DataFrame(columns=['page_number', 'text'])
for i in range(num_of_pages):
    page = pdf.getPage(i)
    text = page.extractText()
    df_text_page.loc[len(df_text_page)] = [i,text]

df_text_page.to_csv('text_by_page.csv')
