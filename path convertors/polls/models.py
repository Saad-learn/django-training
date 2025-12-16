from django.db import models

# Create your models here.
class  Film (models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField()
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name