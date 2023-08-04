from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    type=models.CharField(max_length=20)
class Jobpost(models.Model):
    title=models.TextField()
    company=models.TextField()
    Location=models.TextField()
    Salary=models.IntegerField()
    Description=models.TextField()
    link=models.URLField()
    uid=models.ForeignKey("User",on_delete=models.CASCADE)
