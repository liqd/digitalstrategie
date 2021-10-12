# Generated by Django 3.2.7 on 2021-10-12 11:41

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps_snippets', '0003_fieldofaction'),
        ('apps_forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipationFormPage',
            fields=[
                ('formpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apps_forms.formpage')),
                ('fields_of_action', modelcluster.fields.ParentalManyToManyField(to='apps_snippets.FieldOfAction')),
            ],
            options={
                'abstract': False,
            },
            bases=('apps_forms.formpage',),
        ),
    ]
