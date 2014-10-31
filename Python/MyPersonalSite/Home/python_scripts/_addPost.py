'''
Created on 31-Oct-2014

@author: ghantasa
'''
from Home.models import Post

def addPosttoDB(data):
    try:
#         TODO have to check if post exists and if exists need to update the info.
        Post.objects.get_or_create(
                                    topic = data.topic,
                                    author = data.author,
                                    title = data.title,
                                    tags = data.tags,
                                    gitlink = data.gitlink,
                                    page = data.page,
                                    desc = data.desc,
                                    )
    except Exception as e:
        return e.__str__