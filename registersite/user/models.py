from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class UserDetails(models.Model):

    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
   


  