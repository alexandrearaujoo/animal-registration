# Generated by Django 4.0.5 on 2022-06-14 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_rename_groups_animal_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='characteriscs',
            new_name='characteristics',
        ),
    ]
