# Generated by Django 3.2.7 on 2021-10-01 10:51

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('apps_home', '0005_faq_block'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='body',
            new_name='body_de',
        ),
        migrations.RenameField(
            model_name='homepage',
            old_name='subtitle',
            new_name='subtitle_de',
        ),
        migrations.RenameField(
            model_name='simplepage',
            old_name='body',
            new_name='body_de',
        ),
        migrations.AddField(
            model_name='homepage',
            name='body_en',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('call_to_action', wagtail.blocks.StructBlock([('body', wagtail.blocks.RichTextBlock()), ('link', wagtail.blocks.CharBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50))])), ('image_call_to_action', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=80)), ('body', wagtail.blocks.RichTextBlock()), ('link', wagtail.blocks.CharBlock()), ('link_text', wagtail.blocks.CharBlock(label='Link Text', max_length=50))])), ('columns_text', wagtail.blocks.StructBlock([('columns_count', wagtail.blocks.ChoiceBlock(choices=[(2, 'Two columns'), (3, 'Three columns'), (4, 'Four columns'), (6, 'Six columns')])), ('columns', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock(label='Column body')))])), ('faq_accordion', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=False))]))], blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='subtitle_en',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='simplepage',
            name='body_en',
            field=wagtail.fields.StreamField([('paragraph', wagtail.blocks.RichTextBlock()), ('faq_accordion', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('body', wagtail.blocks.RichTextBlock(required=False))]))], blank=True),
        ),
    ]
