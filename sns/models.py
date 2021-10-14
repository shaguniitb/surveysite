from django.db import models
from django.utils.timezone import now

# Create your models here.

class Comment(models.Model):
    text = models.TextField()
    perspective_score = models.FloatField()
    toxicity_score = models.FloatField()
    author = models.CharField(default = 'Test Author', max_length=100)
    pub_date = models.DateTimeField('date published', default = now)
    num_likes = models.IntegerField(default = 0)
    num_comments = models.IntegerField(default = 0)
    num_retweets = models.IntegerField(default = 0)
    url = models.URLField(blank=True, null=True)
    twitter_id = models.CharField(blank=True, null=True, max_length=100)

class Interface(models.Model):
    name = models.CharField(max_length=100)

class Participant(models.Model):
    username = models.CharField(max_length=100)
    turker_id = models.CharField(max_length=100, blank=True, null=True)
    interface = models.ForeignKey(Interface, blank=True, null=True, on_delete=models.CASCADE)

class ToggleSetting(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    filter_toxic = models.BooleanField(default = False)

class WordFilterSetting(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    word_filters = models.TextField(blank=True, null=True)