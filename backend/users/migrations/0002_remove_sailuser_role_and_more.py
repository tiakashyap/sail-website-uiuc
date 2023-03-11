# Generated by Django 4.1.4 on 2023-03-08 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sailuser',
            name='role',
        ),
        migrations.RemoveField(
            model_name='sailuser',
            name='signed_participant_form',
        ),
        migrations.RemoveField(
            model_name='sailuser',
            name='signed_photo_form',
        ),
        migrations.AddField(
            model_name='sailuser',
            name='admitted_student',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='dietary_restrictions',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='gender_identification',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Non_Binary', 'Non-binary')], default='Male', max_length=10),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='high_school',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailuser',
            name='home_city',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailuser',
            name='home_state',
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='home_zip_code',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailuser',
            name='parent_attending',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='parent_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='parent_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sailuser',
            name='parent_phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='shirt_size',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL')], default='XS', max_length=5),
        ),
        migrations.AddField(
            model_name='sailuser',
            name='year_in_school',
            field=models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior')], default='Freshman', max_length=10),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_attending',
            field=models.BooleanField(blank=True, default=False),
            preserve_default=False,
        ),
    ]