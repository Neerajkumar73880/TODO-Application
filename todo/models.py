from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TODO(models.Model):
    status_choices = [
        ('C','COMPLETED'),
        ('P','PENDING'),
    ]
    priority_choices = [
        ('1','１'),
        ('2','２'),
        ('3','３'),
        ('4','４'),
        ('5','５'),
        ('6','６'),
        ('7','７'),
        ('8','８'),
        ('9','９'),
        ('10','１０'),
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 , choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2 , choices = priority_choices)
    

