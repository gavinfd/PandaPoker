from django.db import models

class Game(models.Model):
	
	def __unicode__(self):
		return self.game_date.strftime('%m/%d/%Y')
	
	def was_played_recently(self):
		return self.game_date >= timezone.now() - datetime.timedelta(days=1)
	was_played_recently.admin_order_field = 'game_date'
	was_played_recently.boolean = True
	was_played_recently.short_description = 'Published recently?'

	variation = models.CharField(max_length=200)
	game_date = models.DateTimeField('date played')
    
class Player(models.Model):
	def __unicode__(self):
		return self.first_name+" "+self.last_name
	
	game = models.ForeignKey(Game)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	standing = models.IntegerField(default=0)

