from django.db import models
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.models import register_setting
from wagtail.documents.edit_handlers import DocumentChooserPanel


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
class Downloads(BaseSetting):
    gruenbuch = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='gruenbuch_pdf'
    )

    panels = [
        DocumentChooserPanel('gruenbuch'),
    ]
