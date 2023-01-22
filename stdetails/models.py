from django.db import models

class Post(models.Model):
    Username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.Username

class details(models.Model):
    Fristname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Pin_no = models.CharField(max_length=50)