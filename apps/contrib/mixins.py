from django.db import models

from apps.contrib.translations import TranslatedField


class TeaserFieldsMixin(models.Model):

    teaser_title_de = models.CharField(max_length=50, blank=True)
    teaser_title_en = models.CharField(max_length=50, blank=True)
    teaser_title_de_ls = models.CharField(max_length=50, blank=True)

    teaser_title = TranslatedField(
        'teaser_title_de',
        'teaser_title_en',
        'teaser_title_de_ls',
    )

    teaser_intro_de = models.TextField(max_length=200, blank=True)
    teaser_intro_en = models.TextField(max_length=200, blank=True)
    teaser_intro_de_ls = models.TextField(max_length=200, blank=True)

    teaser_intro = TranslatedField(
        'teaser_intro_de',
        'teaser_intro_en',
        'teaser_intro_de_ls',
    )

    teaser_image = models.ForeignKey(
        'apps_images.CustomImage',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='+',
        help_text='The image used for the teaser of this page'
    )

    class Meta:
        abstract = True
