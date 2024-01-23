from django.db import models

# Create your models here.
class Msg(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    massage = models.CharField(max_length=200)
