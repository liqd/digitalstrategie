# Generated by Django 3.2.19 on 2023-06-06 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_forms', '0010_add_metatags_to_form_pages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='meta_title_de',
            field=models.CharField(blank=True, help_text='Please note, search engines choose what page information to display based on algorithms for selecting meta tags. Provide relevant and accurate information, but remember that visibility is not guaranteed.', max_length=120, null=True, verbose_name='Meta title de'),
        ),
    ]
