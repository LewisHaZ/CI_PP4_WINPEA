# Generated by Django 3.2.20 on 2023-08-09 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item_catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productitem',
            options={'ordering': ['-item_type']},
        ),
    ]
