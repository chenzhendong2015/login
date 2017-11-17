from django.db import models

class Person(models.Model):
    userName = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    userId = models.CharField(max_length=30)

    def __str__(self):
        return "username: "+self.userName +"  email: "+  self.email
# Create your models here.
