from django.db import models
from user_auth.models import UserAuth
import datetime

# Create your models here.

class Task(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(UserAuth,on_delete=models.CASCADE,related_name='tasks')
    title = models.CharField(max_length=100,db_index=True)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True)
    current_status = models.IntegerField(default=1,choices=[(0, 'In Progress'), (1, 'Pending'), (2, 'Completed'), (3, 'Archived')])
    priority = models.BooleanField(default=True,choices=[(0, 'Low'), (1, 'High')])
    due_date = models.DateField(null=True)
    completion_date = models.DateTimeField(null=True,blank=True)
    
    



