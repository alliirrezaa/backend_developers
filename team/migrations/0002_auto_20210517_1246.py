# Generated by Django 3.2.3 on 2021-05-17 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_member',
            name='instagram_link',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='telegram_link',
            field=models.CharField(max_length=250),
        ),
    ]