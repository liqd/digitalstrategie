from django.utils import translation
from wagtail.core.blocks import CharBlock
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.blocks import StructBlock
from wagtail.core.blocks import StructValue


class TranslatedStructValue(StructValue):

    def link_text(self):
        if translation.get_language() == 'en' and self.get('link_text_en'):
            return self.get('link_text_en')
        else:
            return self.get('link_text_de')


class LinkBlock(StructBlock):
    link = PageChooserBlock(required=True)

    link_text_de = CharBlock(required=True)
    link_text_en = CharBlock(required=False)

    class Meta:
        value_class = TranslatedStructValue
        icon = 'link'
