# Generated by Django 3.2.9 on 2021-12-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20211203_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='active',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]