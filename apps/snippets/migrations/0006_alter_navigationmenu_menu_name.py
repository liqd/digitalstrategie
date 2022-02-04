# Generated by Django 3.2.12 on 2022-02-04 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_snippets', '0005_rename_content_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationmenu',
            name='menu_name',
            field=models.CharField(help_text='Call the menu "header" to use as upper menu. Call the menu "footer" to use asthe upper light grey footer. The lower footer is loaded externally.', max_length=255),
        ),
    ]
