# Generated by Django 4.2.5 on 2023-11-28 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_actionitems_options_alter_gratefulfor_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionitems',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='activities',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='gratefulfor',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='happenings',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='intentions',
            name='ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
