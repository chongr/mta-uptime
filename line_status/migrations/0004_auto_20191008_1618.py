# Generated by Django 2.1.2 on 2019-10-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line_status', '0003_auto_20191008_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linestatus',
            name='created_at',
            field=models.DateTimeField(blank=True),
        ),
    ]
