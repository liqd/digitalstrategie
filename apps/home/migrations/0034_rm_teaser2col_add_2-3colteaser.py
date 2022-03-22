# Generated by Django 3.2.12 on 2022-03-22 14:44

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0033_rm_img_align_add_link_text_teaser_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overviewpage',
            name='body_de',
            field=wagtail.core.fields.StreamField([('teaser_centered', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_columns', wagtail.core.blocks.StructBlock([('column_count', wagtail.core.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup', required=False)), ('column', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='overviewpage',
            name='body_de_ls',
            field=wagtail.core.fields.StreamField([('teaser_centered', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_columns', wagtail.core.blocks.StructBlock([('column_count', wagtail.core.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup', required=False)), ('column', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='overviewpage',
            name='body_en',
            field=wagtail.core.fields.StreamField([('teaser_centered', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=300, rows=3)), ('image', wagtail.images.blocks.ImageChooserBlock()), ('link', wagtail.core.blocks.PageChooserBlock()), ('link_text', wagtail.core.blocks.CharBlock(label='Link Text', max_length=50)), ('background_color', wagtail.core.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_columns', wagtail.core.blocks.StructBlock([('column_count', wagtail.core.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup', required=False)), ('column', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=50)), ('body', wagtail.core.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.core.blocks.StructBlock([('internal_link', wagtail.core.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.core.blocks.URLBlock(required=False)), ('link_text', wagtail.core.blocks.TextBlock(label='Link Text', max_length=50))], help_text='Add either an external or internal link, not both'))])))]))], blank=True),
        ),
    ]