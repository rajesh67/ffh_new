# Generated by Django 2.0 on 2017-12-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiary',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/beneficiaries/'),
        ),
    ]