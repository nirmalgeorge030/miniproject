# Generated by Django 4.2.4 on 2023-08-08 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainerapp', '0002_alter_student_trainer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batch',
            old_name='status',
            new_name='status_id',
        ),
    ]
