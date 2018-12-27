from django.db import models

# Create your models here.
class newsletter_subscriber(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)

class website_recommendation(models.Model):
    website = models.CharField(max_length=128)
    reason = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
