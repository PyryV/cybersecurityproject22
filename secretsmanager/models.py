from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt

class Secret(models.Model):
    title = encrypt(models.TextField())
    classification = models.TextField()
    secret = encrypt(models.TextField())

class UserClearanceLevel(models.Model):
    user_id = models.TextField()
    clearanceLevel = models.TextField()