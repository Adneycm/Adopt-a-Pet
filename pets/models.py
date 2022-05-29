from email import contentmanager
from django.db import models


class Pet(models.Model):
    name = models.TextField()
    type = models.TextField()
    age = models.TextField()
    genre = models.TextField()
    size = models.TextField()
    description = models.TextField()
    img = models.TextField()