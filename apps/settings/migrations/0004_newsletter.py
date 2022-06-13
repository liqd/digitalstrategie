# Generated by Django 3.2.13 on 2022-05-12 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('apps_settings', '0003_accessibility'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sendinblue_api_key', models.CharField(help_text='Your Sendinblue api key', max_length=90)),
                ('sendinblue_list_id', models.PositiveIntegerField(default=0, help_text='The id of the list you want to subscribe to')),
                ('sendinblue_template_id', models.PositiveIntegerField(default=0, help_text='The template id of the newsletter double opt-in')),
                ('redirect_url', models.URLField(help_text='Page being displayed after clicking on link in email')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]