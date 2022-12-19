from django.db import models
from django.contrib.auth.models import User

class Secret(models.Model):
    title = models.TextField()
    classification = models.TextField()
    secret = models.TextField()

class UserClearanceLevel(models.Model):
    user_id = models.TextField()
    clearanceLevel = models.TextField()