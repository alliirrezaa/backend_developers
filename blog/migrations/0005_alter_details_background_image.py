# Generated by Django 3.2.3 on 2021-05-17 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_details_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='%y/%m/%d'),
        ),
    ]