# Generated by Django 3.2.6 on 2022-06-28 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0015_auto_20220627_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]