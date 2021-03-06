# Generated by Django 3.2.7 on 2021-10-26 11:59

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps_snippets', '0004_add_external_subpages_alter_helptexts'),
        ('apps_forms', '0003_formpage_remove_data_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participationformpage',
            name='fields_of_action',
            field=modelcluster.fields.ParentalManyToManyField(help_text='The selected categories                     are displayed in the participation form.', to='apps_snippets.FieldOfAction'),
        ),
    ]
