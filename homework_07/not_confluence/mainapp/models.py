from django.db import models
import datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(unique=True, max_length=20)
    date_create = models.DateTimeField(default=datetime.datetime.now())
    deleted = models.BooleanField()


class Article(models.Model):
    title = models.CharField(unique=True, max_length=30)
    body = models.TextField(blank=True, null=True, max_length=3000)
    date_create = models.DateTimeField(default=datetime.datetime.now())
    deleted = models.BooleanField()
    project_id = models.ForeignKey(Project.id)
    author = models.ForeignKey(User.id)

class User(models.Model):
    login = models.CharField(unique=True, max_length=10)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    date_create = models.DateTimeField(default=datetime.datetime.now())
    deleted = models.BooleanField()

