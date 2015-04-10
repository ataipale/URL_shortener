from django.db import models

# Create your models here.

# my class extends the models function Model class
class Link(models.Model):
    # unique
    # redirect to given link
    # short
    # create these into Django model fields
    unique_ID = models.CharField(max_length = 10, unique = True)
    larger_link = models.URLField()
