# Generated by Django 3.1.3 on 2020-11-20 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatRoom', '0002_auto_20201120_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmodel',
            name='user',
        ),
    ]
