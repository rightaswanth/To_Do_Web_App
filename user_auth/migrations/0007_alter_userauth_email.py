# Generated by Django 5.0.7 on 2024-07-30 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauth',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()]),
        ),
    ]
