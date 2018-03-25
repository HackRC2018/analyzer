from gensim.summarization import keywords
from polyglot.text import Text
from db import connect_db

text = "<p>Contenants scellés, neutres et uniformes, avertissements bien en évidence, espace minimal pour l'affichage du logo et de la marque du fabricant... Santé Canada adoptera des règles semblables à celles entourant l'emballage du tabac pour réglementer l'emballage du cannabis quand il sera légal. Arnaud Granata, éditeur d'Infopresse, et Stéphane Mailhiot, publicitaire, expliquent à Catherine Perrin pourquoi des règles trop strictes pourraient encourager les consommateurs à continuer de s'approvisionner sur le marché noir.</p>"
kw = keywords(text, ratio=0.1, lemmatize=True).split('\n')
str1 = ' '.join(kw)
text = Text(str1, hint_language_code='en')  # switcher a fr
filtre = text.pos_tags

resultat = []

for word in filtre:
    if word[1] == 'NOUN':
        resultat.append(word[0])

print(resultat)