# Generated by Django 2.1.2 on 2019-10-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineStatus',
            fields=[
                ('line_name', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('delayed', models.BooleanField(default=False)),
            ],
        ),
    ]
