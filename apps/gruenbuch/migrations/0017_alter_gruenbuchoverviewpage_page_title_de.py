# Generated by Django 3.2.13 on 2022-05-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_gruenbuch', '0016_remove_colour_from_paragraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='page_title_de',
            field=models.CharField(max_length=120),
        ),
    ]
