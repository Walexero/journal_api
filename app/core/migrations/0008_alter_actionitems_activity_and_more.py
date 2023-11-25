# Generated by Django 4.2.5 on 2023-11-24 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_journal_current_table_alter_journaltables_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionitems',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_items', to='core.activities'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='journal_table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='core.journaltables'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gratefulfor',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grateful_for', to='core.activities'),
        ),
        migrations.AlterField(
            model_name='happenings',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='happenings', to='core.activities'),
        ),
    ]
