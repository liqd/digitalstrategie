from django.core.paginator import InvalidPage
from django.core.paginator import Paginator
from django.db import models
from django.db.models import Q
from django.http import Http404
from django.utils.translation import gettext_lazy as _
from django.utils.translation import ngettext_lazy
from multiselectfield import MultiSelectField
from wagtail import fields
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import FieldRowPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import TabbedInterface
from wagtail.models import Page
from wagtail.search import index

from apps.contrib.mixins import TranslatedMetadataPageMixin
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


class MeasuresOverviewPage(TranslatedMetadataPageMixin, Page):
    template = 'apps_measures/measures_overview_page.html'

    page_swiper = [
        ('image_swiper', apps_blocks.ImageSwiperBlock()),
    ]

    page_teaser = [
        ('teaser_single', apps_blocks.TeaserBlockSingle(
            help_text=_('Only add 1 teaser block per overview page.')
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
        verbose_name=_('Page introduction de'))
    page_intro_en = models.TextField(
        max_length=200,
        blank=True,
        verbose_name=_('Page introduction en'))
    page_intro_de_ls = models.TextField(
        max_length=200,
        blank=True,
        verbose_name=_('Page introduction de ls'))

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
        FieldPanel('title', help_text=_('Add the page title you\'d like '
                   'to be seen in Wagtail in the list of pages.')),
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
        measures_pages = MeasuresDetailPage.objects.live()\
            .descendant_of(self).order_by("title", "-first_published_at")

        return measures_pages

    def _q_filter(self, filter_list, field_name):
        """
        Return Q object for filtering MultiSelectField by list of values.

        filter_list = ['3', '8']
        field_name = 'districts'
        would return
        <Q: (OR: ('districts__contains', '3'), ('districts__contains', '8'))>
        """
        filter_params = Q()
        for element in filter_list:
            kwargs = {'{}__contains'.format(field_name): element}
            filter_params = filter_params | Q(**kwargs)
        return filter_params

    def get_foa_filter_info(self, reg, fut, inc, fac):
        fields_filter_params = Q()
        filter_display_list = []
        if reg:
            fields_filter_params = fields_filter_params | self._q_filter(
                reg, 'regenerative_management'
            )
            for item in reg:
                filter_display_list.append(
                    dict(REGENERATIVE_MANAGEMENT).get(item)
                )
        if fut:
            fields_filter_params = fields_filter_params | self._q_filter(
                fut, 'future_opportunities_for_all'
            )
            for item in fut:
                filter_display_list.append(
                    dict(FUTURE_OPPORTUNITIES_FOR_ALL).get(item)
                )
        if inc:
            fields_filter_params = fields_filter_params | self._q_filter(
                inc, 'inclusive_shaping_of_urban_life'
            )
            for item in inc:
                filter_display_list.append(
                    dict(INCLUSIVE_SHAPING_OF_URBAN_LIFE).get(item)
                )
        if fac:
            fields_filter_params = fields_filter_params | self._q_filter(
                fac, 'facilitative_administration'
            )
            for item in fac:
                filter_display_list.append(
                    dict(FACILITATIVE_ADMINISTRATION).get(item)
                )

        return fields_filter_params, filter_display_list

    def get_context(self, request):
        filtered_measures = self.measures_pages

        # filters for status, district and fields of action (four sets)
        status = request.GET.get('status')
        dis = request.GET.getlist('district')
        reg = request.GET.getlist('reg')
        fut = request.GET.getlist('fut')
        inc = request.GET.getlist('inc')
        fac = request.GET.getlist('fac')

        filter_params = Q()
        filter_display_list = []

        if status and status in dict(STATUS_CHOICES):
            filter_params = filter_params & Q(status=status)
            filter_display_list.append(dict(STATUS_CHOICES).get(status))

        if dis:
            filter_params = filter_params & self._q_filter(dis, 'districts')
            for district in dis:
                filter_display_list.append(dict(BEZIRK_CHOICES).get(district))

        if reg or fut or inc or fac:
            foa_filter_params, foa_filter_display_list = \
                self.get_foa_filter_info(reg, fut, inc, fac)
            filter_params = filter_params & foa_filter_params
            filter_display_list += foa_filter_display_list

        filter_string = ''
        if filter_display_list:
            filter_string = _('Filtered by "{filter_term}".').format(
                filter_term='", "'.join(map(str, filter_display_list))
            )

        # FIXME: when wagtail issue fixed
        # https://github.com/wagtail/wagtail/issues/6616
        measures_page_ids = filtered_measures.filter(
            filter_params).values_list('id', flat=True)
        filtered_measures = filtered_measures.filter(id__in=measures_page_ids)

        # search
        search = request.GET.get('search')
        search_string = ''
        if search:
            filtered_measures = filtered_measures.search(search)
            search_string = _('Search for "{search_term}".').format(
                search_term=search
            )

        # pagination
        page = request.GET.get('page', 1)
        paginator = Paginator(filtered_measures, 6)

        try:
            paginated_measures = paginator.page(page)
        except InvalidPage:
            raise Http404

        # number of results sentence
        result_string = ngettext_lazy(
            '{count} measure.',
            '{count} measures.',
            filtered_measures.count()
        ).format(
            count=str(filtered_measures.count())
        )

        context = super().get_context(request)
        context['measures_pages'] = paginated_measures
        context['selected_districts'] = dis
        context['selected_reg'] = reg
        context['selected_fut'] = fut
        context['selected_inc'] = inc
        context['selected_fac'] = fac
        context['search_string'] = search_string
        context['filter_string'] = filter_string
        context['result_string'] = result_string
        context['filter_count'] = len(filter_display_list)
        return context

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('page_intro_de', partial_match=True),
        index.SearchField('page_intro_en', partial_match=True),
        index.SearchField('page_intro_de_ls', partial_match=True),
    ]


class MeasuresDetailPage(TranslatedMetadataPageMixin, Page):
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
        help_text=_('Up to 3 choices are allowed.')
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
    contact_website_de = models.CharField(max_length=2000, blank=True)

    contact_organisation_name_en = models.CharField(max_length=80, blank=True)
    contact_website_en = models.CharField(max_length=2000, blank=True)

    contact_organisation_name_de_ls = models.CharField(
        max_length=80, blank=True
    )
    contact_website_de_ls = models.CharField(max_length=2000, blank=True)

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
        FieldPanel('title', help_text=_('Add the page title you\'d like '
                   'to be seen in Wagtail in the list of pages.')),
        FieldPanel('slug'),
        FieldPanel('text_image'),
        FieldPanel('districts'),
        FieldPanel('status'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('regenerative_management'),
                FieldPanel('future_opportunities_for_all'),
            ], help_text=_('Up to 3 choices are allowed.'),),
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
        ObjectList(common_panels, heading=_('Common')),
        ObjectList(TranslatedMetadataPageMixin.promote_panels,
                   heading=_('Meta Tags')),
        ObjectList(de_content_panels, heading=_('German')),
        ObjectList(en_content_panels, heading=_('English')),
        ObjectList(de_ls_content_panels, heading=_('Easy German')),
    ])

    search_fields = Page.search_fields + [
        index.SearchField('page_title_de', partial_match=True),
        index.SearchField('page_title_en', partial_match=True),
        index.SearchField('page_title_de_ls', partial_match=True),
        index.SearchField('body_de', partial_match=True),
        index.SearchField('body_en', partial_match=True),
        index.SearchField('body_de_ls', partial_match=True),
        index.SearchField('body_participation_de', partial_match=True),
        index.SearchField('body_participation_en', partial_match=True),
        index.SearchField('body_participation_de_ls', partial_match=True),
        index.SearchField('body_effect_de', partial_match=True),
        index.SearchField('body_effect_en', partial_match=True),
        index.SearchField('body_effect_de_ls', partial_match=True),
        index.SearchField('contact_organisation_name_de', partial_match=True),
        index.SearchField('contact_organisation_name_en', partial_match=True),
        index.SearchField(
            'contact_organisation_name_de_ls', partial_match=True
        ),
        index.SearchField('contact_name', partial_match=True),
    ]

    @property
    def get_fields_of_action(self):
        """Return a dict of selected fields of action and their subsets."""
        fields_of_action = self.get_selected_foa(
            self.regenerative_management, 'reg',
            REGENERATIVE_MANAGEMENT
        ) + self.get_selected_foa(
            self.future_opportunities_for_all, 'fut',
            FUTURE_OPPORTUNITIES_FOR_ALL
        ) + self.get_selected_foa(
            self.inclusive_shaping_of_urban_life, 'inc',
            INCLUSIVE_SHAPING_OF_URBAN_LIFE
        ) + self.get_selected_foa(
            self.facilitative_administration, 'fac',
            FACILITATIVE_ADMINISTRATION
        )
        return fields_of_action

    def get_selected_foa(self, selected_foa_ids, subset_id, subset):
        """Return an object for given fields of action and given subset."""
        selected_foa = []
        for foa_id in selected_foa_ids:
            subset_name = [t[1] for t in subset if t[0] == foa_id][0]
            selected_foa.append({
                'id': foa_id,
                'subset_id': subset_id,
                'subset_name': subset_name
            })
        return selected_foa
