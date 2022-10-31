from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel
from wagtail.admin.panels import InlinePanel
from wagtail.admin.panels import PageChooserPanel
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet

from apps.contrib.translations import TranslatedField
from apps.snippets import blocks as snippets_blocks


class MenuItem(models.Model):

    title_de = models.CharField(
        max_length=255,
    )
    title_en = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )
    title_de_ls = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    link_page = models.ForeignKey(
        'wagtailcore.Page',
        related_name='+',
        blank=True,
        null=True,
        help_text=(
            'Creates a link to a single wagtail page. '
            'Leave empty if you add subpages. '
            'In the footers only subpages will be shown.'
        ),
        on_delete=models.CASCADE
    )

    subpages = StreamField(
        [
            ('link', snippets_blocks.LinkBlock()),
            ('external_link', snippets_blocks.ExternalLinkBlock())
        ],
        blank=True,
        null=True,
        help_text=(
            'These Links will be displayed as sebmenu items. '
            'Either in dropdowns or as items below a headline.'
        ),
        verbose_name='Submenu'
    )

    title = TranslatedField(
        'title_de',
        'title_en',
        'title_de_ls'
    )

    class Meta:
        abstract = True

    @property
    def url(self):
        if self.link_page:
            return self.link_page.url
        return None

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('title_de'),
        FieldPanel('title_en'),
        FieldPanel('title_de_ls'),
        PageChooserPanel('link_page'),
        FieldPanel('subpages')
    ]


class NavigationMenuItem(Orderable, MenuItem):
    parent = ParentalKey('apps_snippets.NavigationMenu',
                         related_name='menu_items')


@register_snippet
class NavigationMenu(ClusterableModel):

    menu_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        help_text=('Call the menu "header" to use as upper menu. '
                   'Call the menu "footer" to use as'
                   'the upper light grey footer. The lower '
                   'footer is loaded externally.')
    )

    def __str__(self):
        return self.menu_name

    panels = [
        FieldPanel('menu_name', classname='full title'),
        InlinePanel('menu_items',
                    label="Menu Items",
                    max_num=6)
    ]


@register_snippet
class FieldOfAction(models.Model):

    name_de = models.CharField(
        max_length=255
    )
    name_en = models.CharField(
        max_length=255,
        blank=True
    )
    name_de_ls = models.CharField(
        max_length=255,
        blank=True
    )

    name = TranslatedField(
        'name_de',
        'name_en',
        'name_de_ls'
    )

    panels = [
        FieldPanel('name_de'),
        FieldPanel('name_en'),
        FieldPanel('name_de_ls')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'fields of action'
