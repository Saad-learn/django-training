from django.db import models
from django.db import models
# Create your models here.
class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to= "images/")

    def __str__ (self):
        return self.title