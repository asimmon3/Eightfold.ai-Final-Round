from django.db import models

# Create your models here.
class AboutYou(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title