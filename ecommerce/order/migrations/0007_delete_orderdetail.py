# Generated by Django 3.0.3 on 2020-04-25 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20200322_0124'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderDetail',
        ),
    ]
