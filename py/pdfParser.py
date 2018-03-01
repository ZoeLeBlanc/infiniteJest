import re
import sys
import textract
import PyPDF2
import pandas as pd
from collections import OrderedDict
from sklearn.feature_extraction.text import CountVectorizer
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph
# pdf = PyPDF2.PdfFileReader(open('David-Foster-Wallace-Infinite-Jest-v2.0.pdf', "rb"))
#
# num_of_pages = pdf.getNumPages()
num_of_pages = pd.read_csv('page_text.csv')
# print(num_of_pages)
# df_text_page = pd.DataFrame(columns=['page_number', 'text'])
df_character_page = pd.DataFrame(columns=['page_number', 'character', 'position'])
#
#
listOfTerms = open('samantha_characters_list.txt')
termRead = listOfTerms.read()
termSplit = termRead.splitlines()
cols = termSplit
cols.insert(0, "page_number")
# # print(cols)
document = []
df_characters_with_page = pd.DataFrame(columns=cols)
for idx, row in num_of_pages.iterrows():
    text = row['text']
    page_terms = ''
    for term in termSplit:
        result = re.search(term.lower(), text.lower())
        if result:
            page_terms += term.replace(" ", "") + ' '
        else:
            pass
    document.append(page_terms)
# document = []
# for i in range(num_of_pages):
#     page = pdf.getPage(i)
#     text = page.extractText()
#     df_text_page.loc[len(df_text_page)] = [i,text]
#     page_terms = ''
#     for term in termSplit:
#         result = re.search(term.lower(), text.lower())
#         if result:
#             # print(term, result.group(0), result.span())
#             # df_character_page.loc[len(df_character_page)] = [i,term, match.span()]
#             # page_terms.append(term)
#             page_terms += term.replace(" ", "") + ' '
#         else:
#             pass
#     document.append(page_terms)
# # print(document)
count_model = CountVectorizer(ngram_range=(1,1)) # default unigram model
X = count_model.fit_transform(document)
# print(X)
Xc = (X.T * X) # this is co-occurrence matrix in sparse csr format
#
Xc.setdiag(0) # sometimes you want to fill same word cooccurence to 0
# vocab = []
# Xc.eliminate_zeros()
# linked = Xc.tolil()
# keys = Xc.todok()
# print(type(keys))
vocab = count_model.vocabulary_
vocab2 = {y:x for x,y in vocab.items()}
G = nx.from_scipy_sparse_matrix(Xc)
H = nx.relabel_nodes(G, vocab2)
# print(list(H.nodes), list(H.edges(data=True)))
data = json_graph.node_link_data(H)
print(data)
T = json_graph.node_link_graph(data)
print(T)
# pos = nx.spring_layout(H)
# nx.draw_networkx_nodes(H, pos, node_size=700)
# elarge = [(u, v) for (u, v, d) in H.edges(data=True) if d['weight'] > 50]
# esmall = [(u, v) for (u, v, d) in H.edges(data=True) if d['weight'] <= 50]
# nx.draw_networkx_edges(H, pos, edgelist=elarge,
#                        width=6)
# nx.draw_networkx_edges(H, pos, edgelist=esmall,
#                        width=6, alpha=0.5, edge_color='b', style='dashed')
# nx.draw_networkx_labels(H, pos, font_size=20, font_family='sans-serif')
#
# plt.axis('off')
# plt.show()
# for v, n in count_model.vocabulary_.items():
#     term = {v: n}
#     print(term)
# print(count_model.vocabulary_, Xc.toarray())
# for x in Xc:
#     print('x',type(x))
#     for i in x:
#         print('i', type(i))
# print(pd.DataFrame(Xc, columns=count_model.get_feature_names()))
# # print(count_model.vocabulary_)
# print(Xc[0:1])
# occurrences = OrderedDict((name, OrderedDict((name, 0) for name in termSplit)) for name in termSplit)
#
# # Find the co-occurrences:
# for l in document:
#     for i in range(len(l)):
#         for item in l[:i] + l[i + 1:]:
#             occurrences[l[i]][item] += 1
#
# # Print the matrix:
# print(' ', ' '.join(occurrences.keys()))
# for name, values in occurrences.items():
#     print(name, ' '.join(str(i) for i in values.values()))
# for i in range(num_of_pages):
#     page = pdf.getPage(i)
#     text = page.extractText()
#     df_text_page.loc[len(df_text_page)] = [i,text]
#     for term in termSplit:
#         for match in re.finditer(term, text):
#             if match:
#                 # print(term, match.group(0), match.span())
#                 df_characters_with_page[len(df)][term] = 1
#                 df_character_page.loc[len(df_character_page)] = [i,term, match.span()]
#             else:
#                 pass
# df_text_page.to_csv('text_by_page.csv')
# df_character_page.to_csv('character_position_by_page.csv')
# df_char_count = df_character_page.groupby(['page_number', 'character']).size().reset_index(name='counts_per_page')
# df_char_count.to_csv('characters_count_by_page.csv')

listOfTerms.close()
