# Generated by Django 4.2.5 on 2023-11-04 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Oldstudents', '0002_rename_field_of_work_student_field_of_study_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='field_of_study',
            new_name='field_of_work',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='gpa',
            new_name='location',
        ),
    ]
