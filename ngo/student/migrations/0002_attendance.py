# Generated by Django 2.2.5 on 2019-09-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField(null=True)),
                ('date', models.DateField()),
                ('status', models.NullBooleanField()),
            ],
        ),
    ]
