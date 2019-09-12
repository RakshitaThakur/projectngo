from django.db import models

class sdata(models.Model):
    rollno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=40)
    fathername = models.CharField(max_length=20)
    mothername = models.CharField(max_length=20)
    phone = models.IntegerField(null=True)

class Attendance(models.Model):
    rollno = models.IntegerField(null=True)
    date = models.DateField()
    status = models.NullBooleanField()
