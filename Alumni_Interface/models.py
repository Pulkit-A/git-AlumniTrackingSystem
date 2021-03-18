from django.db import models
from django.contrib.auth.models import User



class AlumniInfo(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    r_no = models.BigIntegerField(default=None)
    email = models.EmailField()
    course = models.CharField(max_length=20, default=None)
    m_no = models.BigIntegerField()
    org_name = models.CharField(max_length=100, default=None)
    org_add = models.CharField(max_length=100, default=None)
    al_dsg = models.CharField(max_length=50, default=None)
    profile_pic = models.ImageField(null=True, blank=True, default="default.png")
