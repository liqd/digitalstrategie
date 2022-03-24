# Generated by Django 3.2.12 on 2022-03-24 14:50

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps_gruenbuch', '0007_replace_gruenbuch_faq_w_standard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
    ]
