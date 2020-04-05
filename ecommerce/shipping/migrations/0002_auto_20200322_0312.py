# Generated by Django 3.0.3 on 2020-03-22 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='air',
            name='cost',
            field=models.PositiveIntegerField(default=0, help_text='in cents', null=True),
        ),
        migrations.AlterField(
            model_name='ground',
            name='cost',
            field=models.PositiveIntegerField(default=0, help_text='in cents', null=True),
        ),
        migrations.AlterField(
            model_name='sea',
            name='cost',
            field=models.PositiveIntegerField(default=0, help_text='in cents', null=True),
        ),
    ]