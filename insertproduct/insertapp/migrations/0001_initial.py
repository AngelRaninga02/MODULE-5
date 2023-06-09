# Generated by Django 4.1.4 on 2023-02-27 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('companyname', models.CharField(max_length=20)),
                ('selection', models.CharField(max_length=20)),
                ('houseadd', models.TextField()),
                ('apartment', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postcode', models.BigIntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
