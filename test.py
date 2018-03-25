from gensim.summarization import keywords
from polyglot.text import Text


def extract_keywords(text):
    kw = keywords(text, ratio=0.1, lemmatize=True).split('\n')
    str1 = ' '.join(kw)
    text = Text(str1, hint_language_code='fr')  # switch to fr
    filtre = text.pos_tags

    resultat = []

    for word in filtre:
        if word[1] == 'NOUN':
            resultat.append(word[0])

    print(resultat)

text = "Salut je parle de montagne de loup et de nature"
extract_keywords(text)
