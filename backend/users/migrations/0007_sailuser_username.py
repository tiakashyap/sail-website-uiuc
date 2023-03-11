# Generated by Django 4.1.4 on 2023-03-08 21:29

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_sailuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='sailuser',
            name='username',
            field=models.CharField(default=None, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]