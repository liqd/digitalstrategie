# Generated by Django 3.2.12 on 2022-03-28 12:07

import apps.home.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0038_homepage_required_sub_title_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailpage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))]))]),
        ),
        migrations.AlterField(
            model_name='detailpage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='detailpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True)), ('quote', wagtail.core.blocks.CharBlock(required=True)), ('author', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('theses', wagtail.core.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True)), ('quote', wagtail.core.blocks.CharBlock(required=True)), ('author', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('theses', wagtail.core.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('call_to_action', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(required=True)), ('quote', wagtail.core.blocks.CharBlock(required=True)), ('author', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('theses', wagtail.core.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
    ]