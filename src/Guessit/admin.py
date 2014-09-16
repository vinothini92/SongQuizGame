from django.contrib import admin

# Register your models here.
from Guessit.models import Songdata

class SongAdmin(admin.ModelAdmin):
	class Meta:
		model = Songdata

admin.site.register(Songdata)