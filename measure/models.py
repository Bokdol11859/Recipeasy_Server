from django.db import models

# Create your models here.

class Measurement(models.Model):
    title = models.CharField(max_length=20)
    icon_type = models.CharField(max_length=20)
    full = models.CharField(max_length=500)
    full_image = models.URLField()
    half = models.CharField(max_length=500)
    half_image = models.URLField()

    def __str__(self):
        return self.title