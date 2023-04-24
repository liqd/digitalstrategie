from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import FieldRowPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.models import Page
from wagtail.search import index
from wagtailmetadata.models import MetadataPageMixin

from apps.contrib.translations import TranslatedField
from apps.home import blocks as apps_blocks

STATUS_CHOICES = [
    ('1', _('in planning')),
    ('2', _('running')),
    ('3', _('finished')),
]

BEZIRK_CHOICES = [
    ('1', _('gesamtstädtisch')),
    ('2', _('Charlottenburg-Wilmersdorf')),
    ('3', _('Friedrichshain-Kreuzberg')),
    ('4', _('Lichtenberg')),
    ('5', _('Marzahn-Hellersdorf')),
    ('6', _('Mitte')),
    ('7', _('Neukölln')),
    ('8', _('Pankow')),
    ('9', _('Reinickendorf')),
    ('10', _('Spandau')),
    ('11', _('Steglitz-Zehlendorf')),
    ('12', _('Tempelhof-Schöneberg')),
    ('13', _('Treptow-Köpenick')),
]

REGENERATIVE_MANAGEMENT = [
    ('1', _('Smart Economic Models')),
    ('2', _('IT Ecosystems')),
    ('3', _('Smart Capital Region')),
    ('4', _('Regeneration of Natural Resources')),
]

FUTURE_OPPORTUNITIES_FOR_ALL = [
    ('1', _('Capacities for Change')),
    ('2', _('Meeting and Learning Places')),
    ('3', _('Liveable Urban Development')),
    ('4', _('Smart Cities Learning Together')),
]

INCLUSIVE_SHAPING_OF_URBAN_LIFE = [
    ('1', _('Participation')),
    ('2', _('Transparent Decision Processes')),
    ('3', _('Citizen Services')),
    ('4', _('Digital Citizens Rights and Privacy')),
]

FACILITATIVE_ADMINISTRATION = [
    ('1', _('Effective Administrative Processes')),
    ('2', _('Transparent and Innovative Procurement')),
    ('3', _('Intelligent Data Use')),
    ('4', _('Fail-Safe Critical and Digital Infrastructure')),
]


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

    subpage_types = ['apps_measures.MeasuresDetailPage']

    @property
    def status(self):
        return dict(STATUS_CHOICES)

    @property
    def district(self):
        return dict(BEZIRK_CHOICES)

    @property
    def regenerative_management(self):
        return dict(REGENERATIVE_MANAGEMENT)

    @property
    def future_opportunities_for_all(self):
        return dict(FUTURE_OPPORTUNITIES_FOR_ALL)

    @property
    def inclusive_shaping_of_urban_life(self):
        return dict(INCLUSIVE_SHAPING_OF_URBAN_LIFE)

    @property
    def facilitative_administration(self):
        return dict(FACILITATIVE_ADMINISTRATION)

    @property
    def measures_pages(self):
        measures_pages = MeasuresDetailPage.objects.live().descendant_of(self)

        return measures_pages

    def get_context(self, request):
        measures_pages = self.measures_pages
        context = super().get_context(request)
        context['measures_pages'] = measures_pages
        return context

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_intro_de', partial_match=True),
        index.SearchField('page_intro_en', partial_match=True),
        index.SearchField('page_intro_de_ls', partial_match=True),
    ]


class MeasuresDetailPage(Page):
    page_title_de = models.CharField(
        max_length=120, blank=False)
    page_title_en = models.CharField(
        max_length=120, blank=True)
    page_title_de_ls = models.CharField(
        max_length=120, blank=True)

    responsible_organisation_de = models.CharField(
        max_length=80, blank=False)
    responsible_organisation_en = models.CharField(
        max_length=80, blank=True)
    responsible_organisation_de_ls = models.CharField(
        max_length=80, blank=True)

    involved_organisations_de = models.CharField(
        max_length=300, blank=True)
    involved_organisations_en = models.CharField(
        max_length=300, blank=True)
    involved_organisations_de_ls = models.CharField(
        max_length=300, blank=True)

    districts = MultiSelectField(
        blank=True,
        max_choices=3,
        choices=BEZIRK_CHOICES,
        help_text='Up to 3 choices are allowed.'
    )

    regenerative_management = MultiSelectField(
        blank=True,
        max_choices=3,
        choices=REGENERATIVE_MANAGEMENT,
    )

    future_opportunities_for_all = MultiSelectField(
        blank=True,
        max_choices=3,
        choices=FUTURE_OPPORTUNITIES_FOR_ALL,
    )

    inclusive_shaping_of_urban_life = MultiSelectField(
        blank=True,
        max_choices=3,
        choices=INCLUSIVE_SHAPING_OF_URBAN_LIFE,
    )

    facilitative_administration = MultiSelectField(
        blank=True,
        max_choices=3,
        choices=FACILITATIVE_ADMINISTRATION,
    )

    period_de = models.CharField(
        max_length=50, blank=True)
    period_en = models.CharField(
        max_length=50, blank=True)
    period_de_ls = models.CharField(
        max_length=50, blank=True)

    status = models.CharField(max_length=1, blank=True, choices=STATUS_CHOICES)

    text_image = models.ForeignKey(
        'apps_images.CustomImage',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    allowed_features = ['bold', 'italic', 'ol', 'ul', 'hr', 'link',
                        'document-link', 'image', 'embed']

    body_de = fields.RichTextField(blank=False, features=allowed_features)
    body_en = fields.RichTextField(blank=True, features=allowed_features)
    body_de_ls = fields.RichTextField(blank=True, features=allowed_features)

    body_participation_de = fields.RichTextField(blank=True,
                                                 features=allowed_features)
    body_participation_en = fields.RichTextField(blank=True,
                                                 features=allowed_features)
    body_participation_de_ls = fields.RichTextField(blank=True,
                                                    features=allowed_features)

    body_effect_de = fields.RichTextField(blank=True,
                                          features=allowed_features)
    body_effect_en = fields.RichTextField(blank=True,
                                          features=allowed_features)
    body_effect_de_ls = fields.RichTextField(blank=True,
                                             features=allowed_features)

    contact_name = models.CharField(max_length=80, blank=False)
    contact_email = models.CharField(max_length=80, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)

    contact_organisation_name_de = models.CharField(max_length=80, blank=False)
    contact_website_de = models.CharField(max_length=20, blank=True)

    contact_organisation_name_en = models.CharField(max_length=80, blank=True)
    contact_website_en = models.CharField(max_length=20, blank=True)

    contact_organisation_name_de_ls = models.CharField(
        max_length=80, blank=True
    )
    contact_website_de_ls = models.CharField(max_length=20, blank=True)

    page_title = TranslatedField(
        'page_title_de',
        'page_title_en',
        'page_title_de_ls',
    )

    responsible_organisation = TranslatedField(
        'responsible_organisation_de',
        'responsible_organisation_en',
        'responsible_organisation_de_ls',
    )

    involved_organisations = TranslatedField(
        'involved_organisations_de',
        'involved_organisations_en',
        'involved_organisations_de_ls',
    )

    period = TranslatedField(
        'period_de',
        'period_en',
        'period_de_ls',
    )

    body = TranslatedField(
        'body_de',
        'body_en',
        'body_de_ls',
    )

    body_participation = TranslatedField(
        'body_participation_de',
        'body_participation_en',
        'body_participation_de_ls',
    )

    body_effect = TranslatedField(
        'body_effect_de',
        'body_effect_en',
        'body_effect_de_ls',
    )

    contact_organisation_name = TranslatedField(
        'contact_organisation_name_de',
        'contact_organisation_name_en',
        'contact_organisation_name_de_ls',
    )

    contact_website = TranslatedField(
        'contact_website_de',
        'contact_website_en',
        'contact_website_de_ls',
    )

    de_content_panels = [
        FieldPanel('page_title_de'),
        FieldPanel('responsible_organisation_de'),
        FieldPanel('involved_organisations_de'),
        FieldPanel('period_de'),
        FieldPanel('body_de'),
        FieldPanel('body_participation_de'),
        FieldPanel('body_effect_de'),
    ]

    en_content_panels = [
        FieldPanel('page_title_en'),
        FieldPanel('responsible_organisation_en'),
        FieldPanel('involved_organisations_en'),
        FieldPanel('period_en'),
        FieldPanel('body_en'),
        FieldPanel('body_participation_en'),
        FieldPanel('body_effect_en'),
    ]

    de_ls_content_panels = [
        FieldPanel('page_title_de_ls'),
        FieldPanel('responsible_organisation_de_ls'),
        FieldPanel('involved_organisations_de_ls'),
        FieldPanel('period_de_ls'),
        FieldPanel('body_de_ls'),
        FieldPanel('body_participation_de_ls'),
        FieldPanel('body_effect_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('text_image'),
        FieldPanel('districts'),
        FieldPanel('status'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('regenerative_management'),
                FieldPanel('future_opportunities_for_all'),
            ], help_text='Up to 3 choices are allowed.',),
            FieldRowPanel([
                FieldPanel('inclusive_shaping_of_urban_life'),
                FieldPanel('facilitative_administration'),
            ]),
        ], 'handlungsfelder'),
        FieldPanel('contact_organisation_name_de'),
        FieldPanel('contact_organisation_name_en'),
        FieldPanel('contact_organisation_name_de_ls'),
        FieldPanel('contact_name'),
        FieldPanel('contact_email'),
        FieldPanel('contact_phone'),
        FieldPanel('contact_website_de'),
        FieldPanel('contact_website_en'),
        FieldPanel('contact_website_de_ls'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German'),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_en', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True)
    ]
