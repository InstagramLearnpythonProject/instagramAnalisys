import instaparser
import json
from instaparser.agents import Agent
from instaparser.entities import Tag, Media
agent = Agent()
def get_comments_by_tag(tag):
	tag = Tag("tag")
	medias = agent.get_media(obj=tag, count = 10) #get tuple with post identifiers and tag identifier
	for media in medias[0]:
		post = agent.update(obj=Media(media))#get post with comments
		comments=""
		counter =0
		for text in post["edge_media_to_comment"]["edges"]:
			comments += ((text["node"]["text"]) +"\n") #create str from comments
			with open("{}.txt".format(media), "w", encoding = "utf-8" ) as f:
				f.write(comments) 
get_comments_by_tag("copper")
