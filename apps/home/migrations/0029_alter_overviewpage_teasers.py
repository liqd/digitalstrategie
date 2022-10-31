# Generated by Django 3.2.12 on 2022-02-14 13:36

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0028_add_green_colour_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overviewpage',
            name='teasers',
            field=wagtail.fields.StreamField([('teaser_centered', wagtail.blocks.StructBlock([('link', wagtail.blocks.PageChooserBlock(help_text='Make sure that teaser title and teaser intro of the chosen page are set.', page_type=['apps_home.DetailPage', 'apps_forms.FormPage'])), ('link_text_de', wagtail.blocks.CharBlock(label='Link Text de', max_length=50)), ('link_text_en', wagtail.blocks.CharBlock(label='Link Text en', max_length=50, required=False)), ('link_text_de_ls', wagtail.blocks.CharBlock(label='Link Text de ls', max_length=50, required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_two_columns', wagtail.blocks.StructBlock([('link_1', wagtail.blocks.PageChooserBlock(help_text='Make sure that teaser title and teaser intro of the chosen page are set.', page_type=['apps_home.DetailPage', 'apps_forms.FormPage'])), ('link_1_text_de', wagtail.blocks.CharBlock(label='Link Text de', max_length=50)), ('link_1_text_en', wagtail.blocks.CharBlock(label='Link Text en', max_length=50, required=False)), ('link_1_text_de_ls', wagtail.blocks.CharBlock(label='Link Text de ls', max_length=50, required=False)), ('link_2', wagtail.blocks.PageChooserBlock(help_text='Make sure that teaser title and teaser intro of the chosen page are set.', page_type=['apps_home.DetailPage'])), ('link_2_text_de', wagtail.blocks.CharBlock(label='Link Text de', max_length=50)), ('link_2_text_en', wagtail.blocks.CharBlock(label='Link Text en', max_length=50, required=False)), ('link_2_text_de_ls', wagtail.blocks.CharBlock(label='Link Text de ls', max_length=50, required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False))])), ('teaser_image', wagtail.blocks.StructBlock([('link', wagtail.blocks.PageChooserBlock(help_text='Make sure that teaser title, teaser intro and teaser image of the chosen page are set.', page_type=['apps_home.DetailPage', 'apps_forms.FormPage'])), ('link_text_de', wagtail.blocks.CharBlock(label='Link Text de', max_length=50)), ('link_text_en', wagtail.blocks.CharBlock(label='Link Text en', max_length=50, required=False)), ('link_text_de_ls', wagtail.blocks.CharBlock(label='Link Text de ls', max_length=50, required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('pink', 'Pink'), ('purple', 'Purple'), ('green', 'Green')], help_text='Not choosing a colour will result in a block with a white background.', required=False)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))]))]),
        ),
    ]
