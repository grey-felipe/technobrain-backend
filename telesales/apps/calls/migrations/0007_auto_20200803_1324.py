# Generated by Django 3.0.9 on 2020-08-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0006_auto_20200803_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='callback_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
