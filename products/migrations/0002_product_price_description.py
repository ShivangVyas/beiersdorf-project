# Generated by Django 2.1.7 on 2020-03-02 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]