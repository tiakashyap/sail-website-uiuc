# Generated by Django 4.1.4 on 2023-03-08 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_sailuser_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sailuser',
            name='username',
            field=models.CharField(default='', max_length=128, unique=True),
            preserve_default=False,
        ),
    ]