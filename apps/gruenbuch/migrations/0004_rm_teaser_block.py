# Generated by Django 3.2.12 on 2022-03-17 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps_gruenbuch', '0003_add_teaser_fields_to_gruenbuch_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gruenbuchindexpage',
            name='teaser_image',
        ),
        migrations.RemoveField(
            model_name='gruenbuchindexpage',
            name='teaser_intro_de',
        ),
        migrations.RemoveField(
            model_name='gruenbuchindexpage',
            name='teaser_intro_de_ls',
        ),
        migrations.RemoveField(
            model_name='gruenbuchindexpage',
            name='teaser_intro_en',
        ),
        migrations.RemoveField(
            model_name='gruenbuchindexpage',
            name='teaser_title_de',
        ),
        migrations.RemoveField(
            model_name='gruenbuchindexpage',
            name='teaser_title_de_ls',
        ),
        migrations.RemoveField(
            model_name='gruenbuchindexpage',
            name='teaser_title_en',
        ),
    ]
