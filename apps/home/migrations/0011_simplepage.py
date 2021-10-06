# Generated by Django 3.2.7 on 2021-10-06 12:47

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('apps_home', '0010_rename_simplepage_detailpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body_de', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock())])),
                ('body_en', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True)),
                ('body_de_ls', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock())], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
