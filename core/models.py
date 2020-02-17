from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class Member(AbstractUser):

    login = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=500)
    email = models.EmailField(unique=True)
    avatar =  models.ImageField(upload_to='images/avatar/',default='images/avatar/default.png')
    dob = models.DateField(default = timezone.now)

    def __str__(self):
        return self.login

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1000)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
