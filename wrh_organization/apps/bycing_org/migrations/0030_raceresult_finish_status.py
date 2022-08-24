# Generated by Django 4.0.6 on 2022-08-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bycing_org', '0029_alter_raceseriesresult_unique_together_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='raceresult',
            name='finish_status',
            field=models.CharField(choices=[('ok', 'OK'), ('dns', 'DNS'), ('dnf', 'DNF')], default='ok', max_length=16),
        ),
    ]
