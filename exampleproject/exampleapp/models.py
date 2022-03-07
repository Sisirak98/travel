from django.db import models


# Create your models here.
class projecetable(models.Model):
    name = models.CharField(max_length=30)
    ima = models.ImageField(upload_to='im')
    des = models.TextField()

    def __str__(self):
        return self.name


class table2(models.Model):
    nam = models.CharField(max_length=20)
    ima2 = models.ImageField(upload_to='pic')
    des2 = models.TextField()

    def __str__(self):
        return self.nam
