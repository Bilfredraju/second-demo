from django.db import models

# Create your models here.

class data(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    desc=models.CharField(max_length=100)
    fea=models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)+':'+self.name    