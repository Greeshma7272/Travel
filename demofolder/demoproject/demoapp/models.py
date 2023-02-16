from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    dis = models.TextField()

    def __str__(self):
        return self.name


class Meet(models.Model):
    image = models.ImageField(upload_to='pics')
    name = models.CharField(max_length=50)
    dis = models.TextField()

    def __str__(self):
        return self.name


