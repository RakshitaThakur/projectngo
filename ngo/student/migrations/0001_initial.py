# Generated by Django 2.2.5 on 2019-09-12 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sdata',
            fields=[
                ('rollno', models.IntegerField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=40)),
                ('fathername', models.CharField(max_length=20)),
                ('mothername', models.CharField(max_length=20)),
                ('phone', models.IntegerField(null=True)),
            ],
        ),
    ]