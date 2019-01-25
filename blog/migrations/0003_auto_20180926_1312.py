# Generated by Django 2.1.1 on 2018-09-26 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180926_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='body',
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]