# Generated by Django 5.0 on 2023-12-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_alter_versions_options_alter_versions_name_versions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versions',
            name='name_versions',
            field=models.CharField(max_length=150, verbose_name='имя версии'),
        ),
    ]