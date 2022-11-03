# Generated by Django 3.2.16 on 2022-11-08 12:42

from django.db import migrations
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_gruenbuch', '0022_alter_gruenbuchoverviewpage_intro_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_de',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('teaser_columns', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130)), ('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])), ('teaser_tile', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock()), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))])))])), ('video_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Please insert a short description of the video (character limit 255).', max_length=255, required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='You can only add links to YouTube or Vimeo videos.')), ('preview_image', wagtail.images.blocks.ImageChooserBlock(help_text='Add a preview image for the dsgvo video overlay.', required=False)), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], help_text="You can add the video's transcript here (unlimited characters).", required=False))]))], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_de_ls',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('teaser_columns', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130)), ('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])), ('teaser_tile', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock()), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))])))])), ('video_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Please insert a short description of the video (character limit 255).', max_length=255, required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='You can only add links to YouTube or Vimeo videos.')), ('preview_image', wagtail.images.blocks.ImageChooserBlock(help_text='Add a preview image for the dsgvo video overlay.', required=False)), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], help_text="You can add the video's transcript here (unlimited characters).", required=False))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchdetailpage',
            name='body_en',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=False, verbose_name='FAQ Answer'))])))])), ('text_with_image', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(required=True)), ('body', wagtail.blocks.TextBlock(max_length=800, required=True)), ('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'left'), ('right', 'right')], help_text='How should the image be aligned?', icon='cup'))])), ('teaser_columns', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130)), ('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])), ('teaser_tile', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock()), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))])))])), ('video_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Please insert a short description of the video (character limit 255).', max_length=255, required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='You can only add links to YouTube or Vimeo videos.')), ('preview_image', wagtail.images.blocks.ImageChooserBlock(help_text='Add a preview image for the dsgvo video overlay.', required=False)), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], help_text="You can add the video's transcript here (unlimited characters).", required=False))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_de',
            field=wagtail.fields.StreamField([('teaser_columns', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130)), ('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock()), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=False, verbose_name='FAQ Answer'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])), ('video_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Please insert a short description of the video (character limit 255).', max_length=255, required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='You can only add links to YouTube or Vimeo videos.')), ('preview_image', wagtail.images.blocks.ImageChooserBlock(help_text='Add a preview image for the dsgvo video overlay.', required=False)), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], help_text="You can add the video's transcript here (unlimited characters).", required=False))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_de_ls',
            field=wagtail.fields.StreamField([('teaser_columns', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130)), ('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock()), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=False, verbose_name='FAQ Answer'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])), ('video_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Please insert a short description of the video (character limit 255).', max_length=255, required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='You can only add links to YouTube or Vimeo videos.')), ('preview_image', wagtail.images.blocks.ImageChooserBlock(help_text='Add a preview image for the dsgvo video overlay.', required=False)), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], help_text="You can add the video's transcript here (unlimited characters).", required=False))]))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='gruenbuchoverviewpage',
            name='body_en',
            field=wagtail.fields.StreamField([('teaser_columns', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130)), ('column_count', wagtail.blocks.ChoiceBlock(choices=[('2', 'two columns'), ('3', 'three columns')], help_text='Only add this number of columns below', icon='cup')), ('column', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(blank=True, max_length=500, rows=3)), ('button', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])))])), ('teaser_tiles', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=70)), ('tile', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=70)), ('link', wagtail.blocks.PageChooserBlock()), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))])))])), ('paragraph', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=True))])), ('faq_accordion', wagtail.blocks.StructBlock([('faq_title', wagtail.blocks.CharBlock(max_length=150, required=False)), ('accordion_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, verbose_name='FAQ Question')), ('body', wagtail.blocks.RichTextBlock(help_text='For accessibility please make sure that you do not\n                            leave out levels when using the headlines. That\n                            means, that there should always be an h2 before\n                            using an h3.', required=False, verbose_name='FAQ Answer'))])))])), ('teaser_single', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=130)), ('body', wagtail.blocks.TextBlock(max_length=500)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(required=False)), ('external_link', wagtail.blocks.URLBlock(required=False)), ('link_text', wagtail.blocks.TextBlock(label='Link Text', max_length=50)), ('link_description', wagtail.blocks.TextBlock(help_text='describe link for assistive technology if needed', label='Link Description', max_length=70, required=False))], help_text='Add either an external or internal link, not both'))])), ('video_block', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=130, required=False)), ('caption', wagtail.blocks.CharBlock(help_text='Please insert a short description of the video (character limit 255).', max_length=255, required=False)), ('video', wagtail.embeds.blocks.EmbedBlock(help_text='You can only add links to YouTube or Vimeo videos.')), ('preview_image', wagtail.images.blocks.ImageChooserBlock(help_text='Add a preview image for the dsgvo video overlay.', required=False)), ('transcript', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul', 'link', 'document-link'], help_text="You can add the video's transcript here (unlimited characters).", required=False))]))], blank=True, use_json_field=True),
        ),
    ]
