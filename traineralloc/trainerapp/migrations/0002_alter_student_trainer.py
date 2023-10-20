# Generated by Django 4.2.4 on 2023-08-07 09:05

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='trainer',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='CourseName', chained_model_field='CourseName', on_delete=django.db.models.deletion.CASCADE, to='trainerapp.trainer'),
        ),
    ]