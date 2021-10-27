from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.admin.edit_handlers import ObjectList
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.admin.edit_handlers import TabbedInterface
from wagtail.core import blocks
from wagtail.core import fields
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index

from apps.contrib.mixins import TeaserFieldsMixin
from apps.contrib.translations import TranslatedField
from apps.home import blocks as apps_blocks


class GruenbuchIndexPage(Page, TeaserFieldsMixin):
    template = 'gruenbuch_page.html'

    de_content_panels = [
        MultiFieldPanel([
            FieldPanel('teaser_title_de'),
            FieldPanel('teaser_intro_de'),
        ],
            heading="Teaser content",
            classname="collapsible"
        ),
    ]

    en_content_panels = [
        MultiFieldPanel([
            FieldPanel('teaser_title_en'),
            FieldPanel('teaser_intro_en'),
        ],
            heading="Teaser content",
            classname="collapsible"
        ),
    ]

    de_ls_content_panels = [
        MultiFieldPanel([
            FieldPanel('teaser_title_de_ls'),
            FieldPanel('teaser_intro_de_ls'),
        ],
            heading="Teaser content",
            classname="collapsible"
        ),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        ImageChooserPanel('teaser_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    @property
    def book(self):
        return self

    @property
    def chapters(self):
        if self.get_children():
            return self.get_children().specific()

    @property
    def active_chapter(self):
        if self.chapters:
            return self.chapters.first()
        else:
            return ''

    @property
    def next_chapter(self):
        if self.active_chapter:
            return self.active_chapter.get_next_sibling()
        else:
            return ''

    subpage_types = ['apps_gruenbuch.GruenbuchDetailPage']


class GruenbuchDetailPage(Page):
    template = 'gruenbuch_page.html'

    page_blocks = [
        ('paragraph', blocks.RichTextBlock()),
        ('faq_accordion', apps_blocks.GruenbuchFaqBlock())
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

    @property
    def book(self):
        return self.get_parent().specific

    @property
    def chapters(self):
        if self.book.get_children():
            return self.book.get_children().specific()

    @property
    def active_chapter(self):
        return self

    @property
    def next_chapter(self):
        if self.get_next_sibling():
            return self.get_next_sibling().specific
        else:
            return ''

    @property
    def prev_chapter(self):
        if self.get_prev_sibling():
            return self.get_prev_sibling().specific
        else:
            return ''

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('page_title_de_ls',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('page_title_en',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('subtitle_de',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('subtitle_de_ls',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('subtitle_en',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_de', es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_de_ls',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_en', es_extra={'analyzer': 'ngram_analyzer'}),
    ]
