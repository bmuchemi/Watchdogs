# Generated by Django 3.2.6 on 2022-06-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_alter_buisness_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='static/images/jay-eshie-bPYdEoOPo2o-unsplash.jpg', upload_to='static/images/'),
        ),
    ]