from django.db import models

# Create your models here.
class chat(models.Model):
    textline = models.CharField(max_length=3000)
class chat2(models.Model):
    textfie = models.CharField(max_length=3000)
    