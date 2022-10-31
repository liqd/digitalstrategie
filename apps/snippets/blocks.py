from django.utils import translation
from wagtail.blocks import CharBlock
from wagtail.blocks import PageChooserBlock
from wagtail.blocks import StructBlock
from wagtail.blocks import StructValue
from wagtail.blocks import URLBlock


class TranslatedStructValue(StructValue):

    def link_text(self):
        if translation.get_language() == 'en' and self.get('link_text_en'):
            return self.get('link_text_en')
        elif translation.get_language() == 'de-ls' \
                and self.get('link_text_de_ls'):
            return self.get('link_text_de_ls')
        else:
            return self.get('link_text_de')

    def url(self):
        if self.get('link'):
            page = self.get('link')
            return page.url
        else:
            return self.get('external_link')


class LinkBlock(StructBlock):
    link = PageChooserBlock(
        required=True,
    )

    link_text_de = CharBlock(required=True)
    link_text_en = CharBlock(required=False)
    link_text_de_ls = CharBlock(required=False)

    class Meta:
        value_class = TranslatedStructValue
        icon = 'link'


class ExternalLinkBlock(StructBlock):
    external_link = URLBlock(
        required=True,
        help_text=('Please enter a full url which starts with https:// '
                   'or http://'),
        max_length=500,
    )

    link_text_de = CharBlock(required=True)
    link_text_en = CharBlock(required=False)
    link_text_de_ls = CharBlock(required=False)

    class Meta:
        value_class = TranslatedStructValue
        icon = 'link-external'
