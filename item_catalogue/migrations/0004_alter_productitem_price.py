# Generated by Django 3.2.20 on 2023-08-25 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item_catalogue', '0003_productitem_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productitem',
            name='price',
            field=models.IntegerField(),
        ),
    ]
