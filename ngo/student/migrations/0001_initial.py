# Generated by Django 2.2.5 on 2019-11-13 11:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=50)),
                ('fathername', models.CharField(max_length=50)),
                ('mothername', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('status', models.NullBooleanField(default='False')),
                ('rollno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.sdata')),
            ],
        ),
    ]
