# Generated by Django 3.1.3 on 2023-12-13 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songpa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gumodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gunames',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
