# -*- coding: latin-1 -*-

from db import connect_db


# Read file
file = open("histoire.txt", "r", encoding='latin-1')
content = file.read()

# Get id
section_id = 1

# Connect to db
db = connect_db()

# Add text to podcast tags
db.podcasts.find_and_modify(
    query={"id_section": section_id},
    update={"$set": {'text': content}}
)