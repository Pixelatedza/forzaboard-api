# Generated by Django 3.2.9 on 2021-12-16 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0003_remove_record_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='share_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
