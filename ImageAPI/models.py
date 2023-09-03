from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

class Image(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='my_images')

    def __str__(self) -> str:
        return self.name
