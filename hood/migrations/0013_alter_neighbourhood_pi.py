# Generated by Django 3.2.6 on 2022-06-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0012_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='pi',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
