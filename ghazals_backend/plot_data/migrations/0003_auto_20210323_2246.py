# Generated by Django 3.0.5 on 2021-03-24 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plot_data', '0002_auto_20210312_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghazals',
            name='ghazal_content',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
