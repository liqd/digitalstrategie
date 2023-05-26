from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.models import Page
from wagtail.search import index

from apps.contrib.mixins import TranslatedMetadataPageMixin
from apps.contrib.translations import TranslatedField
from apps.home import blocks as apps_blocks


class HomePage(TranslatedMetadataPageMixin, Page):
    # there should only be 1
    max_count = 1
    # only allow as root page
    parent_page_types = ['wagtailcore.Page']
    page_blocks = [
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('quote', apps_blocks.QuoteBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('theses', apps_blocks.ThesisListBlock()),
        ('teaser_image', apps_blocks.TeaserBlockImage()),
        ('teaser_centered', apps_blocks.TeaserBlockCentered()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('newsletter_block', apps_blocks.NewsletterBlock()),
        ('video_block', apps_blocks.VideoBlock())
    ]

    page_title_de = models.CharField(
        max_length=120, blank=False, verbose_name=_('Home page title de'))
    page_title_en = models.CharField(
        max_length=120, blank=True, verbose_name=_('Home page title en'))
    page_title_de_ls = models.CharField(
        max_length=120, blank=True, verbose_name=_('Home page title de ls'))

    page_subtitle_de = models.CharField(
        max_length=255, blank=False, verbose_name=_('Home page subtitle de'))
    page_subtitle_en = models.CharField(
        max_length=255, blank=True, verbose_name=_('Home page subtitle en'))
    page_subtitle_de_ls = models.CharField(
        max_length=255, blank=True, verbose_name=_('Home page subtitle de ls'))

    body_de = fields.StreamField(page_blocks, use_json_field=True)
    body_en = fields.StreamField(page_blocks, blank=True, use_json_field=True)
    body_de_ls = fields.StreamField(
        page_blocks, blank=True, use_json_field=True)

    header_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    ls_header_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    page_title = TranslatedField(
        'page_title_de',
        'page_title_en',
        'page_title_de_ls',
    )

    page_subtitle = TranslatedField(
        'page_subtitle_de',
        'page_subtitle_en',
        'page_subtitle_de_ls',
    )

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('page_subtitle_de'),
        FieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('page_subtitle_en'),
        FieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('page_subtitle_de_ls'),
        FieldPanel('ls_header_image'),
        FieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        FieldPanel('header_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(TranslatedMetadataPageMixin.promote_panels,
                   heading=_('Meta Tags')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    subpage_types = ['apps_home.OverviewPage',
                     'apps_home.DetailPage',
                     'apps_home.SimplePage',
                     'apps_gruenbuch.GruenbuchOverviewPage',
                     'apps_forms.ContactFormPage',
                     'apps_forms.ParticipationFormPage',
                     'apps_home.MicrositeOverviewPage',
                     'apps_home.MicrositeDetailPage',
                     'apps_measures.MeasuresOverviewPage',]

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_subtitle_de', partial_match=True),
        index.SearchField('page_subtitle_en', partial_match=True),
        index.SearchField('page_subtitle_de_ls', partial_match=True),
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_en', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True)
    ]


class OverviewPage(TranslatedMetadataPageMixin, Page):
    teaser_blocks = [
        ('teaser_centered', apps_blocks.TeaserBlockCentered()),
        ('teaser_image', apps_blocks.TeaserBlockImage()),
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_tile', apps_blocks.TeaserBlockTile()),
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('quote', apps_blocks.QuoteBlock()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('newsletter_block', apps_blocks.NewsletterBlock()),
        ('video_block', apps_blocks.VideoBlock())
    ]

    intro_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Intro image is not shown for Easy Language')
    )

    page_title_de = models.CharField(
        max_length=120, blank=False)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    page_intro_de = fields.RichTextField(
        blank=True, default="", verbose_name=_('Overview page introduction'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)
    page_intro_en = fields.RichTextField(
        blank=True, default="", verbose_name=_('Overview page introduction'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)
    page_intro_de_ls = fields.RichTextField(
        blank=True, default="", verbose_name=_('Overview page introduction'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)

    body_de = fields.StreamField(
        teaser_blocks, blank=True, use_json_field=True)
    body_en = fields.StreamField(
        teaser_blocks, blank=True, use_json_field=True)
    body_de_ls = fields.StreamField(
        teaser_blocks, blank=True, use_json_field=True)

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
        FieldPanel('slug'),
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

    subpage_types = ['apps_home.DetailPage',
                     'apps_home.SimplePage',
                     'apps_gruenbuch.GruenbuchOverviewPage',
                     'apps_forms.ContactFormPage',
                     'apps_forms.ParticipationFormPage',
                     'apps_home.MicrositeOverviewPage']

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_intro_de', partial_match=True),
        index.SearchField('page_intro_en', partial_match=True),
        index.SearchField('page_intro_de_ls', partial_match=True),
    ]


class DetailPage(TranslatedMetadataPageMixin, Page):
    page_blocks = [
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('quote', apps_blocks.QuoteBlock()),
        ('newsletter_block', apps_blocks.NewsletterBlock()),
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('video_block', apps_blocks.VideoBlock())
    ]
    page_title_de = models.CharField(
        max_length=120, blank=False)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    body_de = fields.StreamField(page_blocks, use_json_field=True)
    body_en = fields.StreamField(page_blocks, blank=True, use_json_field=True)
    body_de_ls = fields.StreamField(
        page_blocks, blank=True, use_json_field=True)

    page_title = TranslatedField(
        'page_title_de',
        'page_title_en',
        'page_title_de_ls',
    )

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading=_('Common')),
        ObjectList(TranslatedMetadataPageMixin.promote_panels,
                   heading=_('Meta Tags')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_en', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True)
    ]


class SimplePage(TranslatedMetadataPageMixin, Page):
    page_blocks = [
        ('paragraph', blocks.RichTextBlock())
    ]

    page_title_de = models.CharField(
        max_length=120, blank=False)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    body_de = fields.StreamField(page_blocks, use_json_field=True)
    body_en = fields.StreamField(page_blocks, blank=True, use_json_field=True)
    body_de_ls = fields.StreamField(
        page_blocks, blank=True, use_json_field=True)

    page_title = TranslatedField(
        'page_title_de',
        'page_title_en',
        'page_title_de_ls',
    )

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading=_('Common')),
        ObjectList(TranslatedMetadataPageMixin.promote_panels,
                   heading=_('Meta Tags')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_en', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True)
    ]


class MicrositeOverviewPage(TranslatedMetadataPageMixin, Page):
    """
    (Almost) copy of OverviewPage.

    To be used by certain editors, that will only have permission to edit
    Microsite page types.
    """

    template = 'apps_home/overview_page.html'

    teaser_blocks = [
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_tile', apps_blocks.TeaserBlockTile()),
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('quote', apps_blocks.QuoteBlock()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('video_block', apps_blocks.VideoBlock())
    ]

    intro_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text=_('Intro image is not shown for Easy Language')
    )

    page_title_de = models.CharField(
        max_length=120, blank=False)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    page_intro_de = fields.RichTextField(
        blank=True, default="", verbose_name=_('Overview page introduction'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)
    page_intro_en = fields.RichTextField(
        blank=True, default="", verbose_name=_('Overview page introduction'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)
    page_intro_de_ls = fields.RichTextField(
        blank=True, default="", verbose_name=_('Overview page introduction'),
        help_text=apps_blocks.HELPTEXT_RICHTEXT_A11Y)

    body_de = fields.StreamField(
        teaser_blocks, blank=True, use_json_field=True)
    body_en = fields.StreamField(
        teaser_blocks, blank=True, use_json_field=True)
    body_de_ls = fields.StreamField(
        teaser_blocks, blank=True, use_json_field=True)

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
        FieldPanel('slug'),
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

    subpage_types = ['apps_home.MicrositeDetailPage']

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_intro_de', partial_match=True),
        index.SearchField('page_intro_en', partial_match=True),
        index.SearchField('page_intro_de_ls', partial_match=True),
    ]


class MicrositeDetailPage(TranslatedMetadataPageMixin, Page):
    """
    (Almost) copy of DetailPage.

    To be used by certain editors, that will only have permission to edit
    Microsite page types.
    """

    template = 'apps_home/detail_page.html'

    page_blocks = [
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('quote', apps_blocks.QuoteBlock()),
        ('teaser_columns', apps_blocks.TeaserBlockColumn()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('video_block', apps_blocks.VideoBlock())
    ]

    page_title_de = models.CharField(
        max_length=120, blank=False)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    body_de = fields.StreamField(page_blocks, use_json_field=True)
    body_en = fields.StreamField(page_blocks, blank=True, use_json_field=True)
    body_de_ls = fields.StreamField(
        page_blocks, blank=True, use_json_field=True)

    page_title = TranslatedField(
        'page_title_de',
        'page_title_en',
        'page_title_de_ls',
    )

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading=_('Common')),
        ObjectList(TranslatedMetadataPageMixin.promote_panels,
                   heading=_('Meta Tags')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_en', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True)
    ]
