# Generated by Django 3.0.3 on 2020-03-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Air',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('shipment_type', models.CharField(choices=[('ground', 'GROUND'), ('air', 'AIR'), ('sea', 'SEA')], max_length=30)),
                ('cost', models.PositiveIntegerField(help_text='in cents', null=True)),
                ('weight', models.PositiveIntegerField(default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ground',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('shipment_type', models.CharField(choices=[('ground', 'GROUND'), ('air', 'AIR'), ('sea', 'SEA')], max_length=30)),
                ('cost', models.PositiveIntegerField(help_text='in cents', null=True)),
                ('weight', models.PositiveIntegerField(default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('shipment_type', models.CharField(choices=[('ground', 'GROUND'), ('air', 'AIR'), ('sea', 'SEA')], max_length=30)),
                ('cost', models.PositiveIntegerField(help_text='in cents', null=True)),
                ('weight', models.PositiveIntegerField(default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
