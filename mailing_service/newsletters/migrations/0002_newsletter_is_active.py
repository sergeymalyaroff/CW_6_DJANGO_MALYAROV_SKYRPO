# Generated by Django 4.2.5 on 2023-10-13 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]