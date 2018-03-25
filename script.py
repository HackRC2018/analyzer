import requests
import json
import pandas as pd
import urllib2

numero_episode = str(403249)
url_get = 'https://services.radio-canada.ca/hackathon/neuro/v1/episodes/' + numero_episode


# Interrogation API 
emission = requests.get(url_get,
             headers={'Authorization':'Client-Key bf9ac6d8-9ad8-4124-a63c-7b7bdf22a2ee'})

contenu_emission = emission.json()

# Obtention du nom et de l'ID de l'emission'
value1 = pd.DataFrame(contenu_emission.get('ancestors'))
id_emission = str(value1.iloc[0,])
title_emission = value1.iloc[0,4]

# Obtention de l'adresse du podcast a telecharger
value2 = pd.DataFrame(contenu_emission.get('podcastItem'))
lien_url_podcast = str(value2.iloc[1,5])
lien_url_podcast
lien_url_podcast = lien_url_podcast.split("{u'href': u'",1)[1] 
lien_url_podcast = lien_url_podcast.split(".mp3", 1)[0]
lien = lien_url_podcast + '.mp3'

response = requests.get(url_get + '/clips', headers={'Authorization':'Client-Key bf9ac6d8-9ad8-4124-a63c-7b7bdf22a2ee'})
contenu = response.json()

for contentType in contenu:
    print contentType['id'],contentType['title'],contentType['durationInSeconds']


case_list = []
for contentType in contenu:
    image_url = None
    try:
        image_url = contentType['summaryMultimediaItem']['summaryImage']['concreteImages'][0]['mediaLink']['href']
    except Exception:
        pass
    case = [contentType['id'], contentType['title'], contentType['durationInSeconds'], contentType['broadcastedFirstTimeAt'], image_url]
    case_list.append(case)

df = pd.DataFrame(case_list)

df.columns = ['id_section', 'title', 'durationInSeconds',  'broadcastedFirstTimeAt', 'imageUrl']
df = df[df.title.str.contains("Bulletin") == False]
df['fin_seq']=pd.to_numeric(df.durationInSeconds, errors='ignore').cumsum()
df['deb_seq']=df['fin_seq']-pd.to_numeric(df.durationInSeconds, errors='ignore')
df['deb_seq']=df['deb_seq']+1
df.columns = ['id_section', 'title', 'durationInSeconds', 'broadcastedFirstTimeAt', 'imageUrl',  'fin_seq', 'debut_seq']
df['title_emission']=title_emission
df['id_emission']=id_emission
df['id_episode']=numero_episode

print '----------------'
print df