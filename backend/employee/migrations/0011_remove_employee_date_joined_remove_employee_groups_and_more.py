# Generated by Django 5.1.3 on 2024-11-12 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_alter_employee_email_alter_employee_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user_permissions',
        ),
    ]