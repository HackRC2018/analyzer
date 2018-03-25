import time

# from gensim.summarization import keywords
# from polyglot.text import Text
from db import connect_db


DELAY_CHECK_NEW_PODCAST = 10


def extract_keywords(text):
    # kw = keywords(text, ratio=0.1, lemmatize=True).split('\n')
    # str1 = ' '.join(kw)
    # text = Text(str1, hint_language_code='en')  # switch to fr
    # filtre = text.pos_tags

    # resultat = []

    # for word in filtre:
    #     if word[1] == 'NOUN':
    #         resultat.append(word[0])

    # print(resultat)
    # return resultat
    return ['Techno', 'Voiture']


def fill_tags(words):

    db = connect_db()
    tags = db.tags.find()
    tags = [tag['label'] for tag in tags]

    # Check what tags to add 
    tags_to_add = []
    for word in words:
        if word not in tags:
            tags_to_add.append(word)

    # Add new tags to the DB
    for tag in tags_to_add:
        db.tags.insert({'label': tag})

    tags = db.tags.find()
    print(list(tags))


def check_podcasts():
    print('Looking for new podcasts')

    # Get podcasts from DB
    db = connect_db()
    podcasts = db.podcasts.find()

    # Loop on podcasts
    for podcast in podcasts:
        if 'tags' not in podcast:
            print('Extract words for podcast')
            # Extract keywords from summary
            keywords = extract_keywords(podcast['summary'])
            # Add keywords to tags list
            fill_tags(keywords)
            # Add keywords to podcast tags
            db.podcasts.find_and_modify(
                query={"_id": podcast['_id']},
                update={"$set": {'tags': keywords}}
            )


if __name__ == '__main__':
    while True:
        check_podcasts()
        time.sleep(DELAY_CHECK_NEW_PODCAST)
