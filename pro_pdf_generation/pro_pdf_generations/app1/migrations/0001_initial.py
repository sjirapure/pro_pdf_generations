# Generated by Django 4.0.5 on 2022-06-10 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('mail', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
    ]
