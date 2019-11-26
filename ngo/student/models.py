from django.db import models
import datetime

class sdata(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)



class Attendance(models.Model):
    rollno = models.ForeignKey(sdata, on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=datetime.date.today,unique_for_date="True")
    status = models.BooleanField(default="False")

