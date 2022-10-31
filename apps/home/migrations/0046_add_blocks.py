# Generated by Django 3.2.12 on 2022-05-02 10:35

import apps.home.blocks
from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0045_require_column_count_teaser_column_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.fields.StreamField([('call_to_action', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=True)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(required=True)), ('quote', wagtail.blocks.CharBlock(required=True)), ('author', wagtail.blocks.CharBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('theses', wagtail.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_centered', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de_ls',
            field=wagtail.fields.StreamField([('call_to_action', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=True)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(required=True)), ('quote', wagtail.blocks.CharBlock(required=True)), ('author', wagtail.blocks.CharBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('theses', wagtail.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_centered', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.fields.StreamField([('call_to_action', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=True)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('quote', wagtail.blocks.StructBlock([('text', wagtail.blocks.RichTextBlock(required=True)), ('quote', wagtail.blocks.CharBlock(required=True)), ('author', wagtail.blocks.CharBlock(required=False)), ('link', wagtail.blocks.PageChooserBlock(required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('theses', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('theses', wagtail.blocks.ListBlock(apps.home.blocks.ThesisBlock, label='All theses')), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_centered', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='overviewpage',
            name='body_de',
            field=wagtail.fields.StreamField([('teaser_centered', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_columns', wagtail.blocks.StructBlock([('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tile', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(required=True)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='overviewpage',
            name='body_de_ls',
            field=wagtail.fields.StreamField([('teaser_centered', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_columns', wagtail.blocks.StructBlock([('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tile', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(required=True)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='overviewpage',
            name='body_en',
            field=wagtail.fields.StreamField([('teaser_centered', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.blocks.PageChooserBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_columns', wagtail.blocks.StructBlock([('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=50)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tile', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(required=True)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))]))], blank=True),
        ),
    ]
