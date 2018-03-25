# -*- coding: latin-1 -*-
from gensim.summarization import keywords
from polyglot.text import Text


def extract_keywords(text):
    kw = keywords(text, ratio=0.5, lemmatize=True).split('\n')
    str1 = ' '.join(kw)
    text = Text(str1, hint_language_code='fr')  # switch to fr
    filtre = text.pos_tags

    resultat = []

    for word in filtre:
        if word[1] == 'NOUN' and len(word[0]) > 4:
            resultat.append(word[0])
    #print(resultat)


file = open("histoire.txt", "r", encoding='latin-1')
histoire = file.read()

text = "Salut je parle de montagne de loup et de nature"
extract_keywords(histoire)
