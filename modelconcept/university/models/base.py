from django.db import models

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class UpperCaseField(models.CharField):
    def get_prep_value(self, value):
        return value.upper()
