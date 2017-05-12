from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.BigIntegerField(primary_key=True)
    title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.title