# Generated by Django 3.2.5 on 2021-08-08 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210808_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
