# Generated by Django 4.1.4 on 2023-02-09 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycling_org', '0052_merge_20230208_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='rss',
        ),
        migrations.AlterField(
            model_name='organization',
            name='rss_url',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
