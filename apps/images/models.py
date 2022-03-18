from django.db import models
from wagtail.images.models import AbstractImage
from wagtail.images.models import AbstractRendition
from wagtail.images.models import Image

from apps.contrib.translations import TranslatedField


class CustomImage(AbstractImage):

    caption_de = models.CharField(max_length=255, blank=True)
    caption_en = models.CharField(max_length=255, blank=True)
    caption_de_ls = models.CharField(max_length=255, blank=True)

    alt_de = models.CharField(
        max_length=255,
        blank=True,
        help_text='Add an alternative text for image accessibility'
    )
    alt_en = models.CharField(
        max_length=255,
        blank=True,
        help_text='Add an alternative text for image accessibility'
    )
    alt_de_ls = models.CharField(
        max_length=255,
        blank=True,
        help_text='Add an alternative text for image accessibility'
    )

    copyright = models.CharField(
        max_length=255,
        blank=True,
        help_text='Add copyright information for image'
    )

    admin_form_fields = Image.admin_form_fields + (
        'caption_de', 'caption_en', 'caption_de_ls',
        'alt_de', 'alt_en', 'alt_de_ls',
        'copyright'
    )

    caption = TranslatedField(
        'caption_de',
        'caption_en',
        'caption_de_ls',
    )

    alt = TranslatedField(
        'alt_de',
        'alt_en',
        'alt_de_ls'
    )

    @property
    def default_alt_text(self):
        # if this isn't done, the filename is automatically used.
        return self.alt


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage,
                              related_name='renditions',
                              on_delete=models.CASCADE)

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )
