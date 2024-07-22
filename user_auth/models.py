from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True,unique=True)
    first_name = models.CharField(null=False, max_length=100)
    last_name = models.CharField(null=True,max_length=100)
    email = models.CharField(null=False,unique=True, db_index=True,max_length=100)
    hash_password = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

