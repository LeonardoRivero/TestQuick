from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=100, blank=False, unique=True)

    REQUIRED_FIELDS = ['password', 'username']
    USERNAME_FIELD = 'email'

    # def create_user(self, email, username, password=None):
    #     if not email:
    #         raise ValueError("user should have email")
    #     if not username:
    #         raise ValueError("user should have username")
    #     user = self.model(email=email, username=username,)
    #     user.set_password(password)
    #     user.save()
    #     return user

    def __str__(self):
        return str(self.email)
