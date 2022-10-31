# Generated by Django 3.2.13 on 2022-05-06 11:41

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_gruenbuch', '0015_add_single_teaser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_de',
            field=wagtail.fields.StreamField([('teaser_columns', wagtail.blocks.StructBlock([('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for accessible technology', label='Link Description', max_length=70))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for accessible technology', label='Link Description', max_length=70))], help_text='Add either an external or internal link, not both'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_de_ls',
            field=wagtail.fields.StreamField([('teaser_columns', wagtail.blocks.StructBlock([('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for accessible technology', label='Link Description', max_length=70))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for accessible technology', label='Link Description', max_length=70))], help_text='Add either an external or internal link, not both'))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_en',
            field=wagtail.fields.StreamField([('teaser_columns', wagtail.blocks.StructBlock([('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for accessible technology', label='Link Description', max_length=70))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock(page_type=['apps_gruenbuch.GruenbuchDetailPage']))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(required=False, verbose_name='FAQ Answer'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for accessible technology', label='Link Description', max_length=70))], help_text='Add either an external or internal link, not both'))]))], blank=True),
        ),
    ]
