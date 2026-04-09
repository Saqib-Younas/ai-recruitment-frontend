from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model definition
# Humne saari business fields (position, company, etc.) yahan direct add kar di hain
class User(AbstractUser):
    COMPANY_SIZE_CHOICES = [
        ('small', 'Small (1-50)'),
        ('medium', 'Medium (51-200)'),
        ('large', 'Large (200+)'),
    ]
    
    # Email ko unique banaya taaki ye primary identifier/login field ban sake
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    company_size = models.CharField(max_length=10, choices=COMPANY_SIZE_CHOICES, default='small')
    industry_type = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=150, blank=True, null=True)

    # Django ko batana ke email hi username hai login ke liye
    USERNAME_FIELD = 'email'
    
    # Ye fields Django migration ke waqt mangta hai
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email