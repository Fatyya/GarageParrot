# Generated by Django 4.2.4 on 2023-09-04 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0004_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='role',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
