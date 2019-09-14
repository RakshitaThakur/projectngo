from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pics',blank='True')
    college = models.CharField(max_length = 40)
    address = models.CharField(max_length = 300)
    city = models.CharField(max_length = 30)

    def _str_(self):
        return self.user.username