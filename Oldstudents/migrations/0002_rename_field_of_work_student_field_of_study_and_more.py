# Generated by Django 4.2.5 on 2023-11-04 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Oldstudents', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='field_of_work',
            new_name='field_of_study',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='location',
            new_name='gpa',
        ),
        migrations.AddField(
            model_name='student',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='student',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
