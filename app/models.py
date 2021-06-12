from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Complaints(models.Model):
    name = models.CharField(max_length=30)
    webmail = models.EmailField()
    complaint = models.TextField()

    def __str__(self):
        return self.name


class Members(models.Model):
    thumb = models.ImageField(default='default.png', blank=True)
    name = models.CharField(max_length=30)
    webmail = models.EmailField()
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

