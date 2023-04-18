from django.db import models
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.models import Page
from wagtail.search import index
from wagtailmetadata.models import MetadataPageMixin

from apps.contrib.translations import TranslatedField
from apps.home import blocks as apps_blocks


class MeasuresOverviewPage(MetadataPageMixin, Page):
    template = 'apps_measures/measures_overview_page.html'

    page_swiper = [
        ('image_swiper', apps_blocks.ImageSwiperBlock()),
    ]

    page_teaser = [
        ('teaser_single', apps_blocks.TeaserBlockSingle(
            help_text='Only add 1 teaser block per overview page.'
        )),
    ]

    page_title_de = models.CharField(
        max_length=120, blank=False)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    page_intro_de = models.TextField(
        max_length=200,
        blank=False,
        verbose_name="Page introduction de")
    page_intro_en = models.TextField(
        max_length=200,
        blank=True,
        verbose_name="Page introduction en")
    page_intro_de_ls = models.TextField(
        max_length=200,
        blank=True,
        verbose_name="Page introduction de ls")

    swiper_de = fields.StreamField(
        page_swiper, blank=False, use_json_field=True)
    swiper_en = fields.StreamField(
        page_swiper, blank=True, use_json_field=True)
    swiper_de_ls = fields.StreamField(
        page_swiper, blank=True, use_json_field=True)

    teaser_de = fields.StreamField(
        page_teaser, blank=True, use_json_field=True)
    teaser_en = fields.StreamField(
        page_teaser, blank=True, use_json_field=True)
    teaser_de_ls = fields.StreamField(
        page_teaser, blank=True, use_json_field=True)

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

    swiper = TranslatedField(
        'swiper_de',
        'swiper_en',
        'swiper_de_ls',
    )

    teaser = TranslatedField(
        'teaser_de',
        'teaser_en',
        'teaser_de_ls',
    )

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('page_intro_de'),
        FieldPanel('swiper_de'),
        FieldPanel('teaser_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('page_intro_en'),
        FieldPanel('swiper_en'),
        FieldPanel('teaser_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('page_intro_de_ls'),
        FieldPanel('swiper_de_ls'),
        FieldPanel('teaser_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(MetadataPageMixin.promote_panels, heading='Meta Tags'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    # subpage_types = ['']

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_intro_de', partial_match=True),
        index.SearchField('page_intro_en', partial_match=True),
        index.SearchField('page_intro_de_ls', partial_match=True),
    ]
