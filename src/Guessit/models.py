from django.db import models

# Create your models here.
class Songdata(models.Model):
	song_id = models.AutoField(primary_key=True)
	song_name = models.CharField(max_length=256)
	lyrics = models.TextField()
	
	def __unicode__(self):
		return self.song_name