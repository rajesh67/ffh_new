# Generated by Django 2.0 on 2017-12-17 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20171217_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beneficiary',
            name='related_to',
        ),
        migrations.DeleteModel(
            name='Beneficiary',
        ),
    ]
