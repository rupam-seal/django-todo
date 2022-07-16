from django.db import models

# Create your models here.
class Members(models.Model):
    fullname = models.CharField(max_length=255)
    age = models.IntegerField()