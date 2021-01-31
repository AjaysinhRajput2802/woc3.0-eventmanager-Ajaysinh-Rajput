# Generated by Django 3.1.5 on 2021-01-20 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=30)),
                ('fromDt', models.DateTimeField()),
                ('toDt', models.DateTimeField()),
                ('deadline', models.DateTimeField()),
                ('mail', models.EmailField(max_length=254)),
                ('pwd', models.TextField(max_length=10)),
            ],
        ),
    ]
