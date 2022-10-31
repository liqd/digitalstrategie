# Generated by Django 3.2.12 on 2022-03-21 14:27

import apps.home.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0031_add_subtitle_rename_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.fields.StreamField([('call_to_action', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=True)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(required=True)), ('quote', wagtail.blocks.CharBlock(required=True)), ('author', wagtail.blocks.CharBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('theses', wagtail.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de_ls',
            field=wagtail.fields.StreamField([('call_to_action', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=True)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(required=True)), ('quote', wagtail.blocks.CharBlock(required=True)), ('author', wagtail.blocks.CharBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('theses', wagtail.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.fields.StreamField([('call_to_action', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=True)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))]))), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(required=True)), ('quote', wagtail.blocks.CharBlock(required=True)), ('author', wagtail.blocks.CharBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('theses', wagtail.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
    ]
