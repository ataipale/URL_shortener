from django.contrib import admin
from . import models

class LinkAdmin(admin.ModelAdmin):
	model = models.Link 

admin.site.register(models.Link, LinkAdmin)


# Register your models here.
