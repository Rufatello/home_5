# Generated by Django 4.2.7 on 2023-12-01 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_block_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
    ]