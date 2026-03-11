from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    age = models.CharField(max_length=10)
    password = models.CharField(max_length=128)
    date = models.DateField()

    def __str__(self):
     return self.name

