# Generated by Django 3.1.2 on 2020-10-28 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20201028_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='regional_restrictions',
            new_name='job_category',
        ),
        migrations.RemoveField(
            model_name='jobpost',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
