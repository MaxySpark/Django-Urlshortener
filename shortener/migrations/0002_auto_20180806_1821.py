# Generated by Django 2.0.7 on 2018-08-06 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shorturl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
