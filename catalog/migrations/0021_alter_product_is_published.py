# Generated by Django 5.0 on 2023-12-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_alter_product_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='статус публикации'),
        ),
    ]
