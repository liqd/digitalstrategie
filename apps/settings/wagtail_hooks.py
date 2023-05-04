from django.utils.html import escape
from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.documents import get_document_model
from wagtail.rich_text import LinkHandler


class RichtextExternalLinkHandler(LinkHandler):
    identifier = 'external'

    @classmethod
    def expand_db_attributes(cls, attrs):
        href = attrs["href"]
        aria_label_text = _('Opens link in new tab')
        return f'<a href="%s" target="_blank" rel="noreferrer" aria-label="{aria_label_text}">' % escape(href)


class RichtextDocumentLinkHandler(LinkHandler):
    identifier = 'document'

    @staticmethod
    def get_model():
        return get_document_model()

    @classmethod
    def expand_db_attributes(cls, attrs):
        doc = cls.get_instance(attrs)
        aria_label_text = _('Opens document in new tab')
        return f'<a href="%s" target="_blank" aria-label="{aria_label_text}">' % escape(doc.url)


@hooks.register('register_rich_text_features')
def register_external_link(features):
    features.register_link_type(RichtextExternalLinkHandler)


@hooks.register('register_rich_text_features')
def register_document_link(features):
    features.register_link_type(RichtextDocumentLinkHandler)
