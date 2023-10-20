# Generated by Django 4.2.4 on 2023-08-07 08:41

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('trainerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='trainer',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='CourseName', chained_model_field='CourseName', on_delete=django.db.models.deletion.CASCADE, to='trainerapp.trainer'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainerapp.status'),
        ),
    ]