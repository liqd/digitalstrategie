# Generated by Django 3.2.19 on 2023-06-06 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_measures', '0008_make_metatag_fields_not_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measuresdetailpage',
            name='meta_title_de',
            field=models.CharField(blank=True, help_text='Please note, search engines choose what page information to display based on algorithms for selecting meta tags. Provide relevant and accurate information, but remember that visibility is not guaranteed.', max_length=120, null=True, verbose_name='Meta title de'),
        ),
        migrations.AlterField(
            model_name='measuresoverviewpage',
            name='meta_title_de',
            field=models.CharField(blank=True, help_text='Please note, search engines choose what page information to display based on algorithms for selecting meta tags. Provide relevant and accurate information, but remember that visibility is not guaranteed.', max_length=120, null=True, verbose_name='Meta title de'),
        ),
    ]
