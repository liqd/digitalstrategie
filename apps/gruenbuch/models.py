from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.models import Page
from wagtail.search import index
from wagtailmetadata.models import MetadataPageMixin

from apps.contrib.translations import TranslatedField
from apps.home import blocks as apps_blocks


class GruenbuchOverviewPage(MetadataPageMixin, Page):
    template = 'gruenbuch_overview_page.html'

    intro_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Image ratio has to be 2:1 or 4:3. Intro image is not '
                    'shown for Easy Language.')
    )

    page_blocks = [
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_tiles', apps_blocks.TeaserBlockTile()),
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('video_block', apps_blocks.VideoBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
    ]

    page_title_de = models.CharField(
        max_length=120, blank=False)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    page_intro_de = fields.RichTextField(
        blank=True, default="",
        verbose_name=_('Page introduction de'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)
    page_intro_en = fields.RichTextField(
        blank=True, default="",
        verbose_name=_('Page introduction en'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)
    page_intro_de_ls = fields.RichTextField(
        blank=True, default="",
        verbose_name=_('Page introduction de ls'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)

    body_de = fields.StreamField(page_blocks, blank=True, use_json_field=True)
    body_en = fields.StreamField(page_blocks, blank=True, use_json_field=True)
    body_de_ls = fields.StreamField(
        page_blocks, blank=True, use_json_field=True)

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
        FieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('page_intro_en'),
        FieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('page_intro_de_ls'),
        FieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('intro_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading=_('Common')),
        ObjectList(MetadataPageMixin.promote_panels, heading=_('Meta Tags')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    subpage_types = ['apps_gruenbuch.GruenbuchDetailPage',
                     'apps_gruenbuch.GruenbuchIndexPage']

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_intro_de', partial_match=True),
        index.SearchField('page_intro_en', partial_match=True),
        index.SearchField('page_intro_de_ls', partial_match=True),
    ]


class GruenbuchIndexPage(GruenbuchOverviewPage):
    """
    Copy of OverviewPage with new name.

    To be used by as 'chapter overview' page.
    """

    template = 'gruenbuch_overview_page.html'

    class Meta:
        verbose_name = _('Gruenbuch Index Page')

    subpage_types = ['apps_gruenbuch.GruenbuchDetailPage']


class GruenbuchDetailPage(Page):
    template = 'gruenbuch_detail_page.html'

    page_blocks = [
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('teaser_tile', apps_blocks.TeaserBlockTile()),
        ('video_block', apps_blocks.VideoBlock())
    ]

    page_title_de = models.CharField(max_length=120)
    page_title_en = models.CharField(max_length=120, blank=True)
    page_title_de_ls = models.CharField(max_length=120, blank=True)

    subtitle_de = models.CharField(max_length=120, blank=True)
    subtitle_en = models.CharField(max_length=120, blank=True)
    subtitle_de_ls = models.CharField(max_length=120, blank=True)

    body_de = fields.StreamField(page_blocks, use_json_field=True)
    body_en = fields.StreamField(page_blocks, blank=True, use_json_field=True)
    body_de_ls = fields.StreamField(
        page_blocks, blank=True, use_json_field=True)

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
        FieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('subtitle_en'),
        FieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('subtitle_de_ls'),
        FieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading=_('Common')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('subtitle_de', partial_match=True),
        index.SearchField('subtitle_de_ls', partial_match=True),
        index.SearchField('subtitle_en', partial_match=True),
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True),
        index.SearchField('body_en', partial_match=True),
    ]
