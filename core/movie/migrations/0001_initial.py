# Generated by Django 3.2.14 on 2023-11-08 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('tconst', models.CharField(max_length=9, unique=True)),
                ('is_adult', models.BooleanField()),
                ('start_year', models.IntegerField()),
                ('genres', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.genre')),
            ],
        ),
    ]