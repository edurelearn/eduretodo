from statistics import mode
from django.db import models

# Create your models her
class Todosign(models.Model):
   user_name=models.CharField(max_length=100)
   password=models.CharField(max_length=100)
   email_id=models.EmailField()

class usertask(models.Model):
    tasks=models.CharField(max_length=200,default='')
    percentages=models.CharField(max_length=200,default='')
    dates=models.CharField(max_length=200,default='')




