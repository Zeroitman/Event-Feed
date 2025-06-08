from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models


class Achievement(models.Model):
    title = models.CharField(max_length=30)
    condition = models.TextField()
    icon = models.ImageField(upload_to='achievements/')
    created_at = models.DateTimeField(auto_now_add=True)


class UserDjango(PermissionsMixin, AbstractBaseUser):
    password = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(max_length=40, unique=True)
    email = models.EmailField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True


class User(UserDjango):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    achievements = models.ManyToManyField(
        Achievement, related_name='users', blank=True
    )


class Note(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="created by"
    )


class Advertisement(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to='advertisements/')
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
