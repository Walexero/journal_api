# Generated by Django 4.2.5 on 2023-11-27 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_activities_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actionitems',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='gratefulfor',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='happenings',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='intentions',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='actionitems',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tags',
            name='tag_color',
            field=models.CharField(choices=[('Off Gray', 'OFF GRAY'), ('Midnight Green', 'MIDNIGHT GREEN'), ('Wine Red', 'WINE RED'), ('Army Green', 'ARMY GREEN'), ('Yellow', 'YELLOW'), ('Light Blue', 'LIGHT BLUE'), ('Peach', 'PEACH'), ('Teal', 'TEAL'), ('Deep Purple', 'DEEP PURPLE'), ('Brown', 'BROWN')], max_length=30),
        ),
    ]
