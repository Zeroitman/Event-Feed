from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Achievement(models.Model):
    name = models.CharField(max_length=30)
    condition = models.TextField()
    icon = models.ImageField()


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    achievements = models.ManyToManyField(
        Achievement, related_name='users', blank=True
    )


class Note(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    crated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="created by"
    )


class Advertisement(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=225)
    image = models.ImageField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
