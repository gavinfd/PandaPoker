from django.db import models
from apps.variations.models import Variation
from django.contrib.auth.models import User

class Game(models.Model):
    
    def __unicode__(self):
        return self.game_date.strftime('%m/%d/%Y')

    variation = models.ForeignKey(Variation)
    game_date = models.DateTimeField('date played')
    quote = models.CharField(max_length=5000)

class Hand(models.Model):
    def __unicode__(self):
        return self.cards +"; "+self.description
    
    cards = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)

class Player(models.Model):
    def __unicode__(self):
        return self.player.first_name+" "+self.player.last_name
    
    def has_name(self):
        return self.player is not None and self.player.first_name.strip() != ""
    
    game = models.ForeignKey(Game)
    player = models.ForeignKey(User)
    standing = models.IntegerField(default=0)
    knockouts = models.IntegerField(default=0)
    highesthand = models.ForeignKey(Hand, null=True, blank=True)
    

