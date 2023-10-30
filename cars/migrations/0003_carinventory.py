# Generated by Django 4.2.6 on 2023-10-27 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_alter_car_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carinventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_count', models.IntegerField()),
                ('cars_value', models.FloatField()),
                ('created_data', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_data'],
            },
        ),
    ]
