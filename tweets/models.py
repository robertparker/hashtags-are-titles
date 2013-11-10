from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
	tweet_text = models.CharField(max_length=140)
	pub_date = models.DateTimeField('date published')

	def __unicode__(self):
		return self.tweet_text

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Hashtag(models.Model):
	tweet = models.ForeignKey(Tweet)
	hashtag_text = models.CharField(max_length=140)

	def __unicode__(self):
		return self.hashtag_text