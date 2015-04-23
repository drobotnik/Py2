__author__ = 'yahia.abaza'
from nltk.book import *


print('\n*\n*\n*\n')

for i in list(text3)[:10]:
    print(i)


f1 = FreqDist(text3)

print(f1.most_common(50))

print(f1.hapaxes())

long_words = [w for w in set(text3) if len(w)> 10 and w[0] != 'm' and f1[w] > 7]

for word in long_words:
    print(word)


text3.collocations()