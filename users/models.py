from django.db import models
from django.contrib.auth.models import User 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    phone = models.CharField(max_length=15, unique=True)
    license_number = models.CharField(max_length=20, unique=True, default="DEFAULT123")

    def __str__(self):
        return self.user.username
