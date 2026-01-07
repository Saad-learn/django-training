from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)

class Contact(models.Model):
    address = models.CharField(max_length=200)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='article')

    