# Generated by Django 3.2.12 on 2022-05-02 10:35

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_gruenbuch', '0013_require_column_count_teaser_column_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))]))]),
        ),
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.core.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('teaser_columns', wagtail.core.blocks.StructBlock([('column_count', wagtail.core.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=70)), ('tile', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=70)), ('link', wagtail.core.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('teaser_columns', wagtail.core.blocks.StructBlock([('column_count', wagtail.core.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=70)), ('tile', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=70)), ('link', wagtail.core.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('teaser_columns', wagtail.core.blocks.StructBlock([('column_count', wagtail.core.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=70)), ('tile', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=70)), ('link', wagtail.core.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('faq_title', wagtail.core.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.core.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))]))], blank=True),
        ),
    ]
