from django.db import models

# Create your models here.



class Email(models.Model):
    email=models.EmailField()


class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()
