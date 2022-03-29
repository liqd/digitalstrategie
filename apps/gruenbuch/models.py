from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import ObjectList
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.admin.edit_handlers import TabbedInterface
from wagtail.core import blocks
from wagtail.core import fields
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from apps.contrib.translations import TranslatedField
from apps.home import blocks as apps_blocks


class GruenbuchOverviewPage(Page):
    template = 'gruenbuch_overview_page.html'

    intro_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    page_blocks = [
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_tiles', apps_blocks.TeaserBlockTile())
    ]

    page_title_de = models.CharField(
        max_length=120, blank=True)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    page_intro_de = fields.RichTextField(
        blank=True, default="",
        verbose_name="Grünbuch Overview page introduction")
    page_intro_en = fields.RichTextField(
        blank=True, default="",
        verbose_name="Grünbuch Overview page introduction")
    page_intro_de_ls = fields.RichTextField(
        blank=True, default="",
        verbose_name="Grünbuch Overview page introduction")

    body_de = fields.StreamField(page_blocks, blank=True)
    body_en = fields.StreamField(page_blocks, blank=True)
    body_de_ls = fields.StreamField(page_blocks, blank=True)

    page_title = TranslatedField(
        'page_title_de',
        'page_title_en',
        'page_title_de_ls',
    )

    page_intro = TranslatedField(
        'page_intro_de',
        'page_intro_en',
        'page_intro_de_ls'
    )

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('page_intro_de'),
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('page_intro_en'),
        StreamFieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('page_intro_de_ls'),
        StreamFieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        ImageChooserPanel('intro_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    subpage_types = ['apps_gruenbuch.GruenbuchDetailPage']

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de'),
        index.SearchField('page_title_en'),
        index.SearchField('page_title_de_ls'),
        index.SearchField('page_intro_de'),
        index.SearchField('page_intro_en'),
        index.SearchField('page_intro_de_ls'),
    ]


class GruenbuchDetailPage(Page):
    template = 'gruenbuch_detail_page.html'

    page_blocks = [
        ('paragraph', blocks.RichTextBlock()),
        ('faq_accordion', apps_blocks.FaqBlock())
    ]

    page_title_de = models.CharField(max_length=120)
    page_title_en = models.CharField(max_length=120, blank=True)
    page_title_de_ls = models.CharField(max_length=120, blank=True)

    subtitle_de = models.CharField(max_length=120, blank=True)
    subtitle_en = models.CharField(max_length=120, blank=True)
    subtitle_de_ls = models.CharField(max_length=120, blank=True)

    body_de = fields.StreamField(page_blocks)
    body_en = fields.StreamField(page_blocks, blank=True)
    body_de_ls = fields.StreamField(page_blocks, blank=True)

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

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
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

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de'),
        index.SearchField('page_title_de_ls'),
        index.SearchField('page_title_en'),
        index.SearchField('subtitle_de'),
        index.SearchField('subtitle_de_ls'),
        index.SearchField('subtitle_en'),
        index.SearchField('body_de'),
        index.SearchField('body_de_ls'),
        index.SearchField('body_en'),
    ]
