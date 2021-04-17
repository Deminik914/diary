from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=70, blank=True)
    phone = models.CharField(max_length=20)


class School(Contact):
    full_name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=150)
    region = models.CharField(max_length=150)
    district = models.CharField(max_length=150)
    inhabited_locality = models.CharField(max_length=150)

