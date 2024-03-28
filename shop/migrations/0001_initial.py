# Generated by Django 4.2.11 on 2024-03-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=300)),
                ('published_date', models.DateField()),
            ],
        ),
    ]
