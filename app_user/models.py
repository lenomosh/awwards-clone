from django.contrib.auth.models import User
from django.db import models
import math


# Create your models here.
class Project(models.Model):
    image_path = models.CharField(max_length=200)
    description = models.TextField()
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.title


class Profile(models.Model):
    bio = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name


class Rating(models.Model):
    usability, design, content = models.IntegerField(), models.IntegerField(), models.IntegerField()

    def __str__(self):
        return math.fsum([self.usability, self.design, self.content])
