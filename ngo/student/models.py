from django.db import models

class sdata(models.Model):
    rollno = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    mothername = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

class Attendance(models.Model):
    rollno = models.IntegerField(null=True)
    date = models.DateField()
    status = models.NullBooleanField()
