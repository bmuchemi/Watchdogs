# Generated by Django 3.2.6 on 2022-06-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0008_auto_20220627_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buisness',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='neighbourhood',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]
