from django.db import models
from django.contrib.auth.models import User


class UnivInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    univ_name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.BigIntegerField()
    address = models.CharField(max_length=100, default=None)
    profile_pic = models.ImageField(null=True, blank=True, default="default.png")


class EventInfo(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    time = models.CharField(max_length=40)
    img = models.ImageField(null=True, blank=True, default="defaultevent.png")