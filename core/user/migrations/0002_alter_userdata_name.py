# Generated by Django 3.2.14 on 2023-11-10 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
