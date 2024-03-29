# Generated by Django 3.2.7 on 2021-10-07 15:40

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='GruenbuchDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('page_title_de', models.CharField(max_length=120)),
                ('page_title_en', models.CharField(blank=True, max_length=120)),
                ('page_title_de_ls', models.CharField(blank=True, max_length=120)),
                ('subtitle_de', models.CharField(blank=True, max_length=120)),
                ('subtitle_en', models.CharField(blank=True, max_length=120)),
                ('subtitle_de_ls', models.CharField(blank=True, max_length=120)),
                ('body_de', wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('faq_accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))])),
                ('body_en', wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('faq_accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))], blank=True)),
                ('body_de_ls', wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('faq_accordion', wagtail.blocks.StructBlock([('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))], blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GruenbuchIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
