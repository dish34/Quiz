from django.db import models
from django.contrib.auth.models import User

class UserForm(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.EmailField(blank=True)
    total_marks = models.IntegerField(blank=True,default=0)
    Generated_iq = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.user.username
# Create your models here.
