from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import MultiFieldPanel
from wagtailmetadata.models import WagtailImageMetadataMixin
from wagtailmetadata.utils import get_image_model_string

from apps.contrib.translations import TranslatedField


class TranslatedMetadataPageMixin(WagtailImageMetadataMixin, models.Model):
    """An implementation of WagtailImageMetadataMixin for Wagtail pages.

    Like MetadataPageMixin, but with translated meta tags for title and
    description.
    """

    search_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL,
        verbose_name=_('Search image')
    )

    meta_title_de = models.CharField(
        null=True, max_length=120, blank=False,
        verbose_name=_('Meta title de'))
    meta_title_en = models.CharField(
        null=True, max_length=120, blank=True, verbose_name=_('Meta title en'))

    meta_description_de = models.CharField(
        null=True, max_length=255, blank=False,
        verbose_name=_('Meta description de'))
    meta_description_en = models.CharField(
        null=True, max_length=255, blank=True,
        verbose_name=_('Meta description en'))

    meta_title = TranslatedField(
        'meta_title_de',
        'meta_title_en',
        'meta_title_de'  # we only need de and en here, use de for de-ls
    )

    meta_description = TranslatedField(
        'meta_description_de',
        'meta_description_en',
        'meta_description_de'  # we only need de and en here, use de for de-ls
    )

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('meta_title_de'),
            FieldPanel('meta_title_en'),
            FieldPanel('show_in_menus'),
            FieldPanel('meta_description_de'),
            FieldPanel('meta_description_en'),
            FieldPanel('search_image'),
        ], _('Common page configuration')),
    ]

    def get_meta_url(self):
        return self.full_url  # type: ignore

    def get_meta_title(self):
        return self.meta_title

    def get_meta_description(self):
        return self.meta_description

    def get_meta_image(self):
        return self.search_image

    class Meta:
        abstract = True
