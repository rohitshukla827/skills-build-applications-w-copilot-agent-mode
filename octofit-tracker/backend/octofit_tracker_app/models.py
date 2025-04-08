from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField()

class Activity(models.Model):
    user = models.EmailField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    user = models.EmailField()
    points = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
