# Generated by Django 4.2.9 on 2024-03-08 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tree_identification', '0014_delete_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PasswordResetConfirmView',
        ),
    ]