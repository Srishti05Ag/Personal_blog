from django.db import models


class HindiBlog(models.Model):
    title = models.CharField(max_length=255, null=True)
    poem = models.ImageField(upload_to='images/', null=True)
    image = models.ImageField(upload_to='images/', null=True)

    def __str__(self):
        return self.title

