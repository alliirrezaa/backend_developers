# Generated by Django 3.2.3 on 2021-05-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_auto_20210517_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_member',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='%y/%m/%d'),
        ),
    ]
