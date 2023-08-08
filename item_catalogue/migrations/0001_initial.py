# Generated by Django 3.2.20 on 2023-08-03 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200, unique=True)),
                ('price', models.FloatField()),
                ('item_type', models.IntegerField(choices=[(0, 'Necklaces'), (1, 'Bags'), (2, 'Rings'), (3, 'Bracelets'), (4, 'New')], default=4)),
                ('available', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-available'],
            },
        ),
    ]