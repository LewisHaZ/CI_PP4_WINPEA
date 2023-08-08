# Generated by Django 3.2.20 on 2023-08-08 17:46

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('book_a_slot', '0002_booking_people_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('guest_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.RemoveField(
            model_name='booking',
            name='people_count',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='guest_count',
            field=models.IntegerField(choices=[(1, '1 guest'), (2, '2 guests'), (3, '3 guests'), (4, '4 guests'), (5, '5 guests')], default=2),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Awaiting confirmation', 'Awaiting confirmation'), ('Booking accepted', 'Booking accepted'), ('Booking declined', 'Booking declined'), ('Booking expired', 'Booking expired')], default='awaiting confirmation', max_length=25),
        ),
        migrations.AlterField(
            model_name='slot',
            name='max_slots',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='book_a_slot.guest'),
        ),
    ]