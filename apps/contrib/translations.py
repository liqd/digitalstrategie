from django.utils import translation
from wagtail.blocks.stream_block import StreamValue


class TranslatedField(object):

    def __init__(self, de_field, en_field, de_ls_field):
        self.de_field = de_field
        self.en_field = en_field
        self.de_ls_field = de_ls_field

    def hasContent(self, field):
        if isinstance(field, StreamValue):
            return len(field) != 0
        elif isinstance(field, str):
            if field:
                return True
            else:
                return False
        else:
            return False

    def __get__(self, instance, owner):
        de = getattr(instance, self.de_field)
        en = getattr(instance, self.en_field)
        de_ls = getattr(instance, self.de_ls_field)

        if translation.get_language() == 'en' and self.hasContent(en):
            return en
        elif translation.get_language() == 'de-ls' and self.hasContent(de_ls):
            return de_ls
        else:
            return de


def get_search_fields():
    fields = [
        '*page_title_',
        '*page_intro_'
        '*subtitle_',
        '*body_',
    ]
    lang = translation.get_language()
    return [f + lang for f in fields]
