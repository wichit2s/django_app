from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class Member(AbstractUser):

    username = models.CharField(max_length=100, unique=True, verbose_name='ชื่อเข้าใช้งาน')
    first_name = models.CharField(max_length=500, verbose_name='ชื่อ')
    last_name = models.CharField(max_length=500, verbose_name='นามสกุล')
    email = models.EmailField(unique=True, primary_key=True)
    avatar =  models.ImageField(upload_to='images/avatar/',default='images/avatar/default.png')
    dob = models.DateField(default = timezone.now)

    #USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username

class Note(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(blank=True)
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
