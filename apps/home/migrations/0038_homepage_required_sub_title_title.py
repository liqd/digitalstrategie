# Generated by Django 3.2.12 on 2022-03-28 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0037_add_imgtextblock_detail_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='page_subtitle_de',
            field=models.CharField(max_length=255, verbose_name='Home page subtitle de'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='page_title_de',
            field=models.CharField(max_length=120, verbose_name='Home page title de'),
        ),
    ]
