# Generated by Django 3.1.7 on 2021-03-11 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210311_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipaddress',
            old_name='zip_code',
            new_name='zip',
        ),
    ]
