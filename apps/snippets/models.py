from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import InlinePanel
from wagtail.admin.edit_handlers import PageChooserPanel
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable
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
            'In the footer items with subpages will not be shown.'
        ),
        on_delete=models.CASCADE
    )

    subpages = StreamField(
        [
            ('link', snippets_blocks.LinkBlock())
        ],
        blank=True,
        null=True,
        help_text=(
            'These Links will be displayed in a dropdown menu'
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
        StreamFieldPanel('subpages')
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
        help_text=('Call the menu "header" to use as upper menu or '
                   '"footer" to use in the footer.')
    )

    def __str__(self):
        return self.menu_name

    panels = [
        FieldPanel('menu_name', classname='full title'),
        InlinePanel('menu_items',
                    label="Menu Items",
                    max_num=6)
    ]
