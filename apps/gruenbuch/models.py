from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.admin.panels import TitleFieldPanel
from wagtail.admin.widgets.slug import SlugInput
from wagtail.models import Page
from wagtail.search import index

from apps.contrib.mixins import TranslatedMetadataPageMixin
from apps.contrib.translations import TranslatedField
from apps.home import blocks as apps_blocks


class GruenbuchOverviewPage(TranslatedMetadataPageMixin, Page):
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
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_image', apps_blocks.TeaserBlockImage()),
        ('teaser_centered', apps_blocks.TeaserBlockCentered()),
        ('teaser_tiles', apps_blocks.TeaserBlockTile()),
        ('video_block', apps_blocks.VideoBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('quote', apps_blocks.QuoteBlock()),
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
        TitleFieldPanel('title', help_text=_('Add the page title you\'d like '
                        'to be seen in Wagtail in the list of pages.')),
        FieldPanel('slug', widget=SlugInput),
        FieldPanel('intro_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading=_('Common')),
        ObjectList(TranslatedMetadataPageMixin.promote_panels,
                   heading=_('Meta Tags')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    subpage_types = ['apps_gruenbuch.GruenbuchDetailPage',
                     'apps_gruenbuch.GruenbuchIndexPage']

    search_fields = Page.search_fields + [
        index.AutocompleteField('page_title_de'),
        index.AutocompleteField('page_title_en'),
        index.AutocompleteField('page_title_de_ls'),
        index.AutocompleteField('page_intro_de'),
        index.AutocompleteField('page_intro_en'),
        index.AutocompleteField('page_intro_de_ls'),
        index.AutocompleteField('body_de'),
        index.AutocompleteField('body_en'),
        index.AutocompleteField('body_de_ls'),
        index.SearchField('page_title_de'),
        index.SearchField('page_title_en'),
        index.SearchField('page_title_de_ls'),
        index.SearchField('page_intro_de'),
        index.SearchField('page_intro_en'),
        index.SearchField('page_intro_de_ls'),
        index.SearchField('body_de'),
        index.SearchField('body_en'),
        index.SearchField('body_de_ls'),
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


class GruenbuchDetailPage(TranslatedMetadataPageMixin, Page):
    template = 'gruenbuch_detail_page.html'

    page_blocks = [
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_image', apps_blocks.TeaserBlockImage()),
        ('teaser_centered', apps_blocks.TeaserBlockCentered()),
        ('teaser_tiles', apps_blocks.TeaserBlockTile()),
        ('video_block', apps_blocks.VideoBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('quote', apps_blocks.QuoteBlock()),
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
        TitleFieldPanel('title', help_text=_('Add the page title you\'d like '
                        'to be seen in Wagtail in the list of pages.')),
        FieldPanel('slug', widget=SlugInput),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading=_('Common')),
        ObjectList(TranslatedMetadataPageMixin.promote_panels,
                   heading=_('Meta Tags')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    search_fields = Page.search_fields + [
        index.AutocompleteField('page_title_de'),
        index.AutocompleteField('page_title_de_ls'),
        index.AutocompleteField('page_title_en'),
        index.AutocompleteField('subtitle_de'),
        index.AutocompleteField('subtitle_de_ls'),
        index.AutocompleteField('subtitle_en'),
        index.AutocompleteField('body_de'),
        index.AutocompleteField('body_de_ls'),
        index.AutocompleteField('body_en'),
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
