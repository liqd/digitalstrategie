from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtail.admin.panels import ObjectList
from wagtail.admin.panels import PageChooserPanel
from wagtail.admin.panels import TabbedInterface
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.models import register_setting

from apps.contrib.translations import TranslatedField


@register_setting
class ImportantPages(BaseSetting):
    imprint = models.ForeignKey(
        'wagtailcore.Page',
        related_name='important_page_imprint',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    data_protection_policy = models.ForeignKey(
        'wagtailcore.Page',
        related_name='important_page_data_protection_policy',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    panels = [
        PageChooserPanel('imprint',
                         ['apps_home.SimplePage']),
        PageChooserPanel('data_protection_policy',
                         ['apps_home.SimplePage']),
    ]


@register_setting
class Newsletter(BaseSetting):
    sendinblue_api_key = models.CharField(
        max_length=90,
        help_text='Your Sendinblue api key')
    sendinblue_list_id = models.PositiveIntegerField(
        default=0,
        help_text='The id of the list you want to subscribe to')
    sendinblue_template_id = models.PositiveIntegerField(
        default=0,
        help_text='The template id of the newsletter double opt-in')
    redirect_url = models.URLField(help_text="Page being displayed after"
                                             " clicking on link in email")


@register_setting
class Downloads(BaseSetting):
    gruenbuch = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='gruenbuch_pdf'
    )

    panels = [
        FieldPanel('gruenbuch'),
    ]


@register_setting
class Accessibility(BaseSetting):
    feedback_name = models.CharField(max_length=255, blank=True)
    feedback_email = models.EmailField(max_length=255, blank=True)
    feedback_phone = models.CharField(max_length=255, blank=True)

    additional_external_info = models.URLField(
        help_text='Add link to further information',
        blank=True
    )
    additional_external_info_title_de = models.CharField(
        max_length=255, blank=True
    )
    additional_external_info_title_en = models.CharField(
        max_length=255, blank=True
    )
    additional_external_info_title_de_ls = models.CharField(
        max_length=255, blank=True
    )

    accessibility_declaration = models.ForeignKey(
        'wagtailcore.Page',
        related_name='accessibility_declaration_page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    accessibility_declaration_title_de = models.CharField(
        max_length=255, blank=True
    )
    accessibility_declaration_title_en = models.CharField(
        max_length=255, blank=True
    )
    accessibility_declaration_title_de_ls = models.CharField(
        max_length=255, blank=True
    )

    additional_external_info_title = TranslatedField(
        'additional_external_info_title_de',
        'additional_external_info_title_en',
        'additional_external_info_title_de_ls',
    )

    accessibility_declaration_title = TranslatedField(
        'accessibility_declaration_title_de',
        'accessibility_declaration_title_en',
        'accessibility_declaration_title_de_ls',
    )

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('feedback_name'),
                FieldPanel('feedback_email'),
                FieldPanel('feedback_phone')
            ],
            heading="Accessibility Feedback Contact Information",
        ),
        MultiFieldPanel(
            [
                PageChooserPanel('accessibility_declaration',
                                 ['apps_home.SimplePage']),
                FieldPanel('accessibility_declaration_title_de'),
                FieldPanel('accessibility_declaration_title_en'),
                FieldPanel('accessibility_declaration_title_de_ls'),
            ],
            heading="Accessibility Declaration"
        ),
        MultiFieldPanel(
            [
                FieldPanel('additional_external_info'),
                FieldPanel('additional_external_info_title_de'),
                FieldPanel('additional_external_info_title_en'),
                FieldPanel('additional_external_info_title_de_ls'),
            ],
            heading="Further Information on Accessibility"
        )
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Accessibility Information')
    ])
