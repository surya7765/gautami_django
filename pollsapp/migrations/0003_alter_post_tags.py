# Generated by Django 4.2.3 on 2023-07-18 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollsapp', '0002_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
