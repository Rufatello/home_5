# Generated by Django 4.2.7 on 2023-12-01 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_block_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Block',
            new_name='Blog',
        ),
    ]
