# Generated by Django 2.2.7 on 2019-11-20 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191119_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='advert',
            name='img',
            field=models.ImageField(upload_to='advert/%Y/%m/%d'),
        ),
    ]