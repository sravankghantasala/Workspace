from django.db import models

# Create your models here.

topic_choice = ( ('p', 'python'), ('j', 'java'), ('c', 'c++'), ('b', 'bash'), ('m', 'misc') )
author_choice = ( ('s','Sravan K Ghantasala'), ('p','Praveen kumar Ghantasala'))


class Post(models.Model):
    topic = models.CharField(max_length=15, choices=topic_choice, default='p')
    author = models.CharField(max_length=30,choices = author_choice, default='s')
    git_link = models.URLField(max_length=200)
    page = models.FilePathField(max_length=200)
    desc = models.TextField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    edit_time = models.DateTimeField(auto_now=True)
    