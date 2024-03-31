


from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.CharField(max_length=255)
    publication_date = models.DateField(blank=True, null=True)
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
