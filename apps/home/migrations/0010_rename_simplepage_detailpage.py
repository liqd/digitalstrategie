# Generated by Django 3.2.7 on 2021-10-06 12:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('apps_home', '0009_faq_block_styling_color'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SimplePage',
            new_name='DetailPage',
        ),
    ]
