from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser 

from django.contrib.auth.models import Group , Permission


class AdminUser(AbstractUser):
    first_name = models.CharField(max_length=254, default="" , null=True , blank=True)
    last_name = models.CharField(max_length=254, default="", null=True , blank=True)
    email = models.EmailField(max_length=254, default="", null=True , blank=True)
    phone = models.CharField(max_length=254, default="", null=True , blank=True)

    facebook = models.CharField(max_length=254, default="https://facebook.com", null=True , blank=True)
    twitter = models.CharField(max_length=254, default="https://twitter.com", null=True , blank=True)
    instagram = models.CharField(max_length=254, default="https://instagram.com", null=True , blank=True)
    linkedin = models.CharField(max_length=254, default="https://linkedin.com", null=True , blank=True)

    groups = models.ManyToManyField(Group, related_name='admin_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='admin_user_permissions' )


    def check_password(self, raw_password: str) -> bool:
        return super().check_password(raw_password) 

    def set_password(self, raw_password: str) -> None:
        return super().set_password(raw_password)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    class Meta : 
        db_table='admin_user'
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}" 


