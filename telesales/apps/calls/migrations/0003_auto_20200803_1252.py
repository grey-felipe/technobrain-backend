# Generated by Django 3.0.9 on 2020-08-03 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0002_auto_20200803_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='callback_date',
            field=models.DateTimeField(null=True),
        ),
    ]
