# Generated by Django 3.2.7 on 2021-10-25 13:44

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('apps_snippets', '0003_fieldofaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationmenu',
            name='menu_name',
            field=models.CharField(help_text='Call the menu "header" to use as upper menu or "footer" to use in the lower dark grey footer. To display the upper light grey footer, call the menu snippet “content-footer”.', max_length=255),
        ),
        migrations.AlterField(
            model_name='navigationmenuitem',
            name='link_page',
            field=models.ForeignKey(blank=True, help_text='Creates a link to a single wagtail page. Leave empty if you add subpages. In the footers only subpages will be shown.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page'),
        ),
        migrations.AlterField(
            model_name='navigationmenuitem',
            name='subpages',
            field=wagtail.core.fields.StreamField([('link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.PageChooserBlock(required=True)), ('link_text_de', wagtail.core.blocks.CharBlock(required=True)), ('link_text_en', wagtail.core.blocks.CharBlock(required=False)), ('link_text_de_ls', wagtail.core.blocks.CharBlock(required=False))])), ('external_link', wagtail.core.blocks.StructBlock([('external_link', wagtail.core.blocks.URLBlock(help_text='Please enter a full url which starts with https:// or http://', max_length=500, required=True)), ('link_text_de', wagtail.core.blocks.CharBlock(required=True)), ('link_text_en', wagtail.core.blocks.CharBlock(required=False)), ('link_text_de_ls', wagtail.core.blocks.CharBlock(required=False))]))], blank=True, help_text='These Links will be displayed as sebmenu items. Either in dropdowns or as items below a headline.', null=True, verbose_name='Submenu'),
        ),
    ]
