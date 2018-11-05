import re
import os
import instaparser
from instaparser.agents import Agent
from instaparser.entities import Tag, Media

def preprocess_text(text):
    text = text.lower().replace("ё", "е")
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
    text = re.sub('@[^\s]+', 'USER', text)
    text = re.sub('#[^\s]+', 'TAG', text)
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub('[a-zA-Z]+', ' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip()

agent = Agent()

def get_comments_by_tag(word, numberOfPost):
    try:
        os.mkdir("{}".format(word))
    except FileExistsError:
    	pass
    tag = Tag(word)
    medias = agent.get_media(obj=tag, count = numberOfPost ) #get tuple with post identifiers and tag identifier
    counter = 0
    for media in medias[0]:
        post = agent.update(obj=Media(media))#get post with comments
        if post["edge_media_to_comment"]["edges"] != []:
            counter += 1
            comments = ""
            with open("{}/{}.txt".format(word, media), "w", encoding = "utf-8", ) as f:
                for t in post["edge_media_to_comment"]["edges"]:
                    comment = str(t["node"]["text"]) #create str from 
                    comment = preprocess_text(comment)
                    comments = (comment + "\n")
                    f.write(comments)
    return counter

get_comments_by_tag("гальванопластика", 5)
print(get_comments_by_tag("гальванопластика", 5))