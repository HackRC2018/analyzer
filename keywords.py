# -*- coding: utf-8 -*-

from gensim.summarization import keywords
from polyglot.text import Text

#lire le dataset de texte
file = open("dagon.txt", "r")
dagon = file.read()

file = open("mountain.txt", "r")
mountain = file.read()

file = open("azathoth.txt", "r")
azathoth = file.read()

file = open("alchemist.txt", "r")
alchemist = file.read()


kw = keywords(azathoth, ratio=0.1, lemmatize=True).split('\n')

str1 = ' '.join(kw)

text = Text(str1, hint_language_code='en') #switcher a fr

filtre = text.pos_tags

resultat = []

for word in filtre:
    if word[1] == 'NOUN':
        #print(word)[0]
        resultat.append(word[0])

print(resultat)