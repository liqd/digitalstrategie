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
from wagtailmetadata.models import MetadataPageMixin

from apps.contrib.translations import TranslatedField
from apps.home import blocks as apps_blocks


class HomePage(MetadataPageMixin, Page):
    page_blocks = [
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('quote', apps_blocks.QuoteBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('theses', apps_blocks.ThesisListBlock()),
        ('teaser_image', apps_blocks.TeaserBlockImage()),
        ('teaser_centered', apps_blocks.TeaserBlockCentered()),
        ('teaser_single', apps_blocks.TeaserBlockSingle()),
        ('newsletter_block', apps_blocks.NewsletterBlock()),
    ]

    page_title_de = models.CharField(
        max_length=120, blank=False, verbose_name=('Home page title de'))
    page_title_en = models.CharField(
        max_length=120, blank=True, verbose_name=('Home page title en'))
    page_title_de_ls = models.CharField(
        max_length=120, blank=True, verbose_name=('Home page title de ls'))

    page_subtitle_de = models.CharField(
        max_length=255, blank=False, verbose_name=('Home page subtitle de'))
    page_subtitle_en = models.CharField(
        max_length=255, blank=True, verbose_name=('Home page subtitle en'))
    page_subtitle_de_ls = models.CharField(
        max_length=255, blank=True, verbose_name=('Home page subtitle de ls'))

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
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('page_subtitle_en'),
        StreamFieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('page_subtitle_de_ls'),
        StreamFieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        ImageChooserPanel('header_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(MetadataPageMixin.promote_panels, heading='Meta Tags'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    subpage_types = ['apps_home.OverviewPage',
                     'apps_home.DetailPage',
                     'apps_home.SimplePage',
                     'apps_gruenbuch.GruenbuchOverviewPage',
                     'apps_forms.ContactFormPage',
                     'apps_forms.ParticipationFormPage']

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


class OverviewPage(MetadataPageMixin, Page):
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
    ]

    intro_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    background_color = models.CharField(
        choices=apps_blocks.ColorChoiceBlock.choices,
        help_text='This sets the background colour of the introduction part '
                  'of this page. Not choosing a colour will result in '
                  'a white background.',
        blank=True,
        max_length=50
    )

    page_title_de = models.CharField(
        max_length=120, blank=True)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    page_intro_de = fields.RichTextField(
        blank=True, default="", verbose_name="Overview page introduction")
    page_intro_en = fields.RichTextField(
        blank=True, default="", verbose_name="Overview page introduction")
    page_intro_de_ls = fields.RichTextField(
        blank=True, default="", verbose_name="Overview page introduction")

    body_de = fields.StreamField(teaser_blocks, blank=True)
    body_en = fields.StreamField(teaser_blocks, blank=True)
    body_de_ls = fields.StreamField(teaser_blocks, blank=True)

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
        FieldPanel('background_color'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(MetadataPageMixin.promote_panels, heading='Meta Tags'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    subpage_types = ['apps_home.DetailPage',
                     'apps_home.SimplePage',
                     'apps_gruenbuch.GruenbuchOverviewPage',
                     'apps_forms.ContactFormPage',
                     'apps_forms.ParticipationFormPage']

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_intro_de', partial_match=True),
        index.SearchField('page_intro_en', partial_match=True),
        index.SearchField('page_intro_de_ls', partial_match=True),
    ]


class DetailPage(Page):
    page_blocks = [
        ('paragraph', apps_blocks.ParagraphBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('quote', apps_blocks.QuoteBlock()),
        ('newsletter_block', apps_blocks.NewsletterBlock()),
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

    search_fields = Page.search_fields + [
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_en', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True)
    ]


class SimplePage(Page):
    page_blocks = [
        ('paragraph', blocks.RichTextBlock())
    ]

    page_title_de = models.CharField(
        max_length=120, blank=True)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    body_de = fields.StreamField(page_blocks)
    body_en = fields.StreamField(page_blocks, blank=True)
    body_de_ls = fields.StreamField(page_blocks, blank=True)

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
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        StreamFieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
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

    search_fields = Page.search_fields + [
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_en', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True)
    ]
