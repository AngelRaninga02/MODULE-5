# Generated by Django 4.1.4 on 2023-02-24 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('product_dicription', models.TextField()),
            ],
        ),
    ]
