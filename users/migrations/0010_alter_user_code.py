# Generated by Django 5.0 on 2023-12-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(default='09469', max_length=15, verbose_name='код'),
        ),
    ]
