from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROLES = (("0", "Admin"), ("1", "User"))
    role = models.CharField(max_length=1, choices= ROLES, default="1")
    email = models.EmailField(verbose_name= "email", max_length= 255, unique= True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = "username", "role", "first_name", "last_name"

    def __str__(self):
        return self.username
    
