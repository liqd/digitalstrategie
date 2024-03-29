# Generated by Django 3.2.16 on 2022-10-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_forms', '0008_alter_formpage_header_de'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='choices',
            field=models.TextField(blank=True, help_text='Comma or new line separated list of choices. Only applicable in checkboxes, radio and dropdown.', verbose_name='choices'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='default_value',
            field=models.TextField(blank=True, help_text='Default value. Comma or new line separated values supported for checkboxes.', verbose_name='default value'),
        ),
    ]
