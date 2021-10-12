# Generated by Django 3.2.7 on 2021-10-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps_snippets', '0002_add_simple_german_to_menu'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldOfAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_de', models.CharField(max_length=255)),
                ('name_en', models.CharField(blank=True, max_length=255)),
                ('name_de_ls', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'fields of action',
            },
        ),
    ]
