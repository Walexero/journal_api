# Generated by Django 4.2.5 on 2023-12-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_alter_journaltables_options_journaltables_table_func'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journaltables',
            name='table_func',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]