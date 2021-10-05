from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import ObjectList
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.admin.edit_handlers import TabbedInterface
from wagtail.core import blocks, fields
from wagtail.core.models import Page

from apps import blocks as apps_blocks
from apps.contrib.translations import TranslatedField

class GruenbuchIndexPage(Page):

    subpage_types = ['apps_gruenbuch.GruenbuchDetailPage']

class GruenbuchDetailPage(Page):

    page_blocks = [
        ('paragraph', blocks.RichTextBlock()),
        ('faq_accordion', apps_blocks.FaqBlock())
    ]

    page_title_de = models.CharField(max_length=120, blank=True)
    page_title_en = models.CharField(max_length=120, blank=True)
    page_title_de_ls = models.CharField(max_length=120, blank=True)

    subtitle_de = models.CharField(max_length=120, blank=True)
    subtitle_en = models.CharField(max_length=120, blank=True)
    subtitle_de_ls = models.CharField(max_length=120, blank=True)

    body_de = fields.StreamField(page_blocks, blank=True)
    body_en = fields.StreamField(page_blocks, blank=True)
    body_de_ls = fields.StreamField(page_blocks, blank=True)

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    page_title = TranslatedField(
        'page_title_de',
        'page_title_en',
        'page_title_de_ls',
    )

    subtitle = TranslatedField(
        'subtitle_de',
        'subtitle_en',
        'subtitle_de_ls',
    )

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('subtitle_de'),
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('subtitle_en'),
        StreamFieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('subtitle_de_ls'),
        StreamFieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    subpage_types = []
