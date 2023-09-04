# Generated by Django 4.2.4 on 2023-08-30 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('garage', '0003_alter_staff_role_customuser_alter_staff_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='customuser_group_set', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='The permissions this user has.', related_name='customuser_set', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
