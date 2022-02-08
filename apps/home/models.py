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


class HomePage(Page):
    page_blocks = [
        ('call_to_action', apps_blocks.CallToActionBlock()),
        ('faq_accordion', apps_blocks.FaqBlock()),
        ('quote', apps_blocks.QuoteBlock()),
        ('text_with_image', apps_blocks.TextWithImageBlock()),
        ('theses', apps_blocks.ThesisListBlock())
    ]

    subtitle_de = models.CharField(
        max_length=120, blank=True, verbose_name=('Home page title de'))
    subtitle_en = models.CharField(
        max_length=120, blank=True, verbose_name=('Home page title en'))
    subtitle_de_ls = models.CharField(
        max_length=120, blank=True, verbose_name=('Home page title de ls'))

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

    subpage_types = ['apps_home.OverviewPage',
                     'apps_home.DetailPage',
                     'apps_home.SimplePage',
                     'apps_gruenbuch.GruenbuchIndexPage',
                     'apps_forms.ContactFormPage',
                     'apps_forms.ParticipationFormPage']

    search_fields = Page.search_fields + [
        index.SearchField('subtitle_de',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('subtitle_en',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('subtitle_de_ls',
                          es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_de', es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_en', es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_de_ls',
                          es_extra={'analyzer': 'ngram_analyzer'})
    ]


class OverviewPage(Page):
    teaser_blocks = [
        ('teaser_centered', apps_blocks.TeaserBlockCentered()),
        ('teaser_two_columns', apps_blocks.TeaserBlockTwoColumns()),
        ('teaser_image', apps_blocks.TeaserBlockImage()),
        ('paragraph', apps_blocks.CoulouredParagraphBlock()),
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

    teasers = fields.StreamField(teaser_blocks)

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('page_intro_de')
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('page_intro_en')
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('page_intro_de_ls')
    ]

    common_panels = [
        FieldPanel('title'),
        ImageChooserPanel('intro_image'),
        FieldPanel('background_color'),
        StreamFieldPanel('teasers'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    subpage_types = ['apps_home.DetailPage',
                     'apps_home.SimplePage',
                     'apps_gruenbuch.GruenbuchIndexPage',
                     'apps_forms.ContactFormPage',
                     'apps_forms.ParticipationFormPage']


class DetailPage(Page, TeaserFieldsMixin):
    page_blocks = [
        ('paragraph', apps_blocks.CoulouredParagraphBlock()),
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
        MultiFieldPanel([
            FieldPanel('teaser_title_de'),
            FieldPanel('teaser_intro_de'),
        ],
            heading="Teaser content",
            classname="collapsible"
        ),
        StreamFieldPanel('body_de'),
    ]

    en_content_panels = [
        MultiFieldPanel([
            FieldPanel('teaser_title_en'),
            FieldPanel('teaser_intro_en'),
        ],
            heading="Teaser content",
            classname="collapsible"
        ),
        StreamFieldPanel('body_en'),
    ]

    de_ls_content_panels = [
        MultiFieldPanel([
            FieldPanel('teaser_title_de_ls'),
            FieldPanel('teaser_intro_de_ls'),
        ],
            heading="Teaser content",
            classname="collapsible"
        ),
        StreamFieldPanel('body_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        ImageChooserPanel('teaser_image'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    subpage_types = []

    search_fields = Page.search_fields + [
        index.SearchField('body_de', es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_en', es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_de_ls',
                          es_extra={'analyzer': 'ngram_analyzer'})
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
        index.SearchField('body_de', es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_en', es_extra={'analyzer': 'ngram_analyzer'}),
        index.SearchField('body_de_ls',
                          es_extra={'analyzer': 'ngram_analyzer'})
    ]
