# Generated by Django 3.1.4 on 2020-12-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ledger', '0003_auto_20201201_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankaccountmodel',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bankaccountmodel',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]
