from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='covers/', null=True, blank=True)
    file = models.FileField(upload_to='books/')
    number_of_pages = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title
