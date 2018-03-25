import requests
import pandas as pd

from db import connect_db


def fetch_data_emission(numero_episode):
    url_get = 'https://services.radio-canada.ca/hackathon/neuro/v1/episodes/' + numero_episode

    # Interrogation API
    emission = requests.get(url_get, headers={'Authorization': 'Client-Key bf9ac6d8-9ad8-4124-a63c-7b7bdf22a2ee'})

    contenu_emission = emission.json()

    # Obtention du nom et de l'ID de l'emission'
    value1 = pd.DataFrame(contenu_emission.get('ancestors'))
    id_emission = str(value1.iloc[0,])
    title_emission = value1.iloc[0,4]

    response = requests.get(url_get + '/clips', headers={'Authorization': 'Client-Key bf9ac6d8-9ad8-4124-a63c-7b7bdf22a2ee'})
    contenu = response.json()

    for contentType in contenu:
        print(contentType['id'], contentType['title'],contentType['durationInSeconds'])

    case_list = []
    for contentType in contenu:
        image_url = None
        try:
            image_url = contentType['summaryMultimediaItem']['summaryImage']['concreteImages'][0]['mediaLink']['href']
        except Exception:
            pass
        case = [contentType['id'], contentType['title'], contentType['durationInSeconds'], contentType['broadcastedFirstTimeAt'], contentType['summary'], image_url]
        case_list.append(case)

    df = pd.DataFrame(case_list)

    df.columns = ['id_section', 'title', 'durationInSeconds',  'broadcastedFirstTimeAt', 'summary', 'imageUrl']
    df = df[df.title.str.contains("Bulletin") == False]
    df['fin_seq'] = pd.to_numeric(df.durationInSeconds, errors='ignore').cumsum()
    df['deb_seq'] = df['fin_seq']-pd.to_numeric(df.durationInSeconds, errors='ignore')
    df['deb_seq'] = df['deb_seq']+1
    df.columns = ['id_section', 'title', 'durationInSeconds', 'broadcastedFirstTimeAt', 'summary', 'imageUrl',  'fin_seq', 'debut_seq']
    df['title_emission'] = title_emission
    df['id_emission'] = id_emission
    df['id_episode'] = numero_episode

    return df


def insert_to_db(data):
    db = connect_db()
    db.podcasts.insert_many(data.to_dict('records'))

numero_episode = str(403249)

data = fetch_data_emission(numero_episode)
print(data)
# insert_to_db(data)
