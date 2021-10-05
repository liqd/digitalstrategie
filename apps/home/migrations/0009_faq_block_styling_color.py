# Generated by Django 3.2.7 on 2021-10-05 14:00

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0008_add_language_easy_german'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50))])), ('image_call_to_action', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=80)), ('body', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50))])), ('columns_text', wagtail.core.blocks.StructBlock([('columns_count', wagtail.core.blocks.ChoiceBlock(choices=[(2, 'Two columns'), (3, 'Three columns'), (4, 'Four columns'), (6, 'Six columns')])), ('columns', wagtail.core.blocks.ListBlock(wagtail.core.blocks.RichTextBlock(label='Column body')))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50))])), ('image_call_to_action', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=80)), ('body', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50))])), ('columns_text', wagtail.core.blocks.StructBlock([('columns_count', wagtail.core.blocks.ChoiceBlock(choices=[(2, 'Two columns'), (3, 'Three columns'), (4, 'Four columns'), (6, 'Six columns')])), ('columns', wagtail.core.blocks.ListBlock(wagtail.core.blocks.RichTextBlock(label='Column body')))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('call_to_action', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50))])), ('image_call_to_action', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=80)), ('body', wagtail.core.blocks.RichTextBlock()), ('link', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50))])), ('columns_text', wagtail.core.blocks.StructBlock([('columns_count', wagtail.core.blocks.ChoiceBlock(choices=[(2, 'Two columns'), (3, 'Three columns'), (4, 'Four columns'), (6, 'Six columns')])), ('columns', wagtail.core.blocks.ListBlock(wagtail.core.blocks.RichTextBlock(label='Column body')))])), ('faq_accordion', wagtail.core.blocks.StructBlock([('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))]),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('faq_accordion', wagtail.core.blocks.StructBlock([('accordion_items', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.RichTextBlock(required=False))]))), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple')], help_text='Not choosing a colour will result in an FAQ block with a white background.', required=False))]))], blank=True),
        ),
    ]
