# Generated by Django 3.1.2 on 2020-10-20 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20201020_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='./trousers/'),
        ),
    ]
