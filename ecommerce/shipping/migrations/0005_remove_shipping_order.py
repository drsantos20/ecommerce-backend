# Generated by Django 3.0.3 on 2020-07-05 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0004_auto_20200505_0436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='order',
        ),
    ]
