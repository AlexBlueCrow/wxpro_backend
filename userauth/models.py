from django.db import models
from django.utils import timezone
# Create your models here.
class User(models.Model):
    openid = models.CharField(max_length = 50,unique = True)
    created_date = models.DateTimeField(auto_now_add=True)
    
