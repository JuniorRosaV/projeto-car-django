# Generated by Django 4.2.6 on 2023-10-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField()),
                ('model_year', models.IntegerField()),
                ('plate', models.CharField(max_length=7)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='cars/')),
                ('value', models.FloatField()),
                ('biography', models.TextField()),
            ],
        ),
    ]
