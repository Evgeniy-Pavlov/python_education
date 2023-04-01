from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    login = models.CharField(unique=True, max_length=10)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    date_create = models.DateTimeField(null=True)


class Project(models.Model):
    name = models.CharField(unique=True, max_length=20)
    user_create = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_create = models.DateTimeField(null=True) 
    user_update = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_projects')
    date_update = models.DateTimeField(null=True, blank=True)


class Article(models.Model):
    title = models.CharField(unique=True, max_length=30)
    body = models.TextField(blank=True, null=True, max_length=3000)
    date_create = models.DateTimeField(null=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, null=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    user_update = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_articles')
    date_update = models.DateTimeField(null=True, blank=True)




