from django.db import models
from django.contrib.auth.models import User
from variations.models import Variation
from django.utils import timezone
import datetime

class Game(models.Model):
	
	def __unicode__(self):
		return self.game_date.strftime('%m/%d/%Y')
	
	def was_played_recently(self):
		return self.game_date >= timezone.now() - datetime.timedelta(days=1)
	was_played_recently.admin_order_field = 'game_date'
	was_played_recently.boolean = True
	was_played_recently.short_description = 'Published recently?'

	variation = models.ForeignKey(Variation)
	game_date = models.DateTimeField('date played')

class Hand(models.Model):
	def __unicode__(self):
		return self.cards +"; "+self.description
	
	cards = models.CharField(max_length=200)
	description = models.CharField(max_length=200)

class Player(models.Model):
	def __unicode__(self):
		return self.player.first_name+" "+self.player.last_name
	
	game = models.ForeignKey(Game)
	player = models.ForeignKey(User)
	standing = models.IntegerField(default=0)
	knockouts = models.IntegerField(default=0)
	highesthand = models.ForeignKey(Hand)
	


