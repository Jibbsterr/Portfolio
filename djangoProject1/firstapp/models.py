from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True, default=None)
    phone = models.CharField(max_length=30)
    concern = models.TextField(null=True, blank=True, default=None)



