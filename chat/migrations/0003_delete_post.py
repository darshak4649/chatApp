# Generated by Django 4.2.9 on 2024-02-12 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_users'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]