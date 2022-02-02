# Generated by Django 3.2.12 on 2022-02-03 10:17

import apps.home.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0025_add_link_to_text_with_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True)), ('quote', wagtail.core.blocks.CharBlock(required=True)), ('author', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('theses', wagtail.core.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True)), ('quote', wagtail.core.blocks.CharBlock(required=True)), ('author', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('theses', wagtail.core.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True)), ('quote', wagtail.core.blocks.CharBlock(required=True)), ('author', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('theses', wagtail.core.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
    ]
