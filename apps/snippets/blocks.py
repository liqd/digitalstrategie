from wagtail.core.blocks import CharBlock
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.blocks import StructBlock

from apps.contrib.translations import TranslatedField


class LinkBlock(StructBlock):
    link = PageChooserBlock(required=True)

    link_text_de = CharBlock(required=True)
    link_text_en = CharBlock(required=False)

    link_text = TranslatedField(
        'link_text_de',
        'link_text_en'
    )
