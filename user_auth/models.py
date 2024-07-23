from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    first_name = models.CharField(null=False, max_length=100, unique=True)
    last_name = models.CharField(null=True,max_length=100,blank=True)
    email = models.EmailField(null=False,unique=True, db_index=True, max_length=100)
    hash_password = models.CharField(max_length=255)
    username = models.CharField(max_length=100,default="aliaz")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)

