# Generated by Django 3.2.19 on 2023-06-06 12:46

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_measures', '0008_make_metatag_fields_not_required'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measuresoverviewpage',
            name='swiper_de',
            field=wagtail.fields.StreamField([('image_swiper', wagtail.blocks.StructBlock([('swiper_item', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=100)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=250, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))], help_text='Please note that images will be displayed in a 16:9 aspect ratio. Crop or resize your images accordingly before uploading to ensure they display correctly.')))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='measuresoverviewpage',
            name='swiper_de_ls',
            field=wagtail.fields.StreamField([('image_swiper', wagtail.blocks.StructBlock([('swiper_item', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=100)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=250, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))], help_text='Please note that images will be displayed in a 16:9 aspect ratio. Crop or resize your images accordingly before uploading to ensure they display correctly.')))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='measuresoverviewpage',
            name='swiper_en',
            field=wagtail.fields.StreamField([('image_swiper', wagtail.blocks.StructBlock([('swiper_item', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=100)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=250, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))], help_text='Please note that images will be displayed in a 16:9 aspect ratio. Crop or resize your images accordingly before uploading to ensure they display correctly.')))]))], blank=True, use_json_field=True),
        ),
    ]
