from django.db import models

class TODO(models.Model):
    sno=models.AutoField(primary_key=True,auto_created=True)
    title=models.CharField(max_length=100)
    desc=models.TextField()
    date=models.DateField(auto_now_add=True)
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)

class signup(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)    
# Create your models here.
