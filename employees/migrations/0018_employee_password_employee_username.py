# Generated by Django 4.2.5 on 2023-10-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_alter_employee_age_alter_employee_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
