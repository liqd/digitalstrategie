from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import ObjectList
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.admin.edit_handlers import TabbedInterface
from wagtail.core import blocks
from wagtail.core import fields
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from apps import blocks as apps_blocks
from apps.contrib.translations import TranslatedField


class HomePage(Page):

    page_blocks = [
        ('paragraph', blocks.RichTextBlock()),
        ('call_to_action', apps_blocks.CallToActionBlock()),
        ('image_call_to_action', apps_blocks.ImageCallToActionBlock()),
        ('columns_text', apps_blocks.ColumnsBlock()),
        ('faq_accordion', apps_blocks.FaqBlock())
    ]

    subtitle_de = models.CharField(max_length=120, blank=True)
    subtitle_en = models.CharField(max_length=120, blank=True)
    subtitle_de_ls = models.CharField(max_length=120, blank=True)

    body_de = fields.StreamField(page_blocks)
    body_en = fields.StreamField(page_blocks, blank=True)
    body_de_ls = fields.StreamField(page_blocks, blank=True)

    header_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    subtitle = TranslatedField(
        'subtitle_de',
        'subtitle_en',
        'subtitle_de_ls',
    )

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    de_content_panels = [
        FieldPanel('subtitle_de'),
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('subtitle_en'),
        StreamFieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('subtitle_de_ls'),
        StreamFieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        ImageChooserPanel('header_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    subpage_types = ['apps_home.DetailPage', 'apps_home.SimplePage']


class DetailPage(Page):

    page_blocks = [
        ('paragraph', blocks.RichTextBlock()),
        ('faq_accordion', apps_blocks.FaqBlock())
    ]

    body_de = fields.StreamField(page_blocks)
    body_en = fields.StreamField(page_blocks, blank=True)
    body_de_ls = fields.StreamField(page_blocks, blank=True)

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    de_content_panels = [
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        StreamFieldPanel('body_en'),
    ]

    de_ls_content_panels = [
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


class SimplePage(Page):

    page_blocks = [
        ('paragraph', blocks.RichTextBlock())
    ]

    body_de = fields.StreamField(page_blocks)
    body_en = fields.StreamField(page_blocks, blank=True)
    body_de_ls = fields.StreamField(page_blocks, blank=True)

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    de_content_panels = [
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        StreamFieldPanel('body_en'),
    ]

    de_ls_content_panels = [
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
