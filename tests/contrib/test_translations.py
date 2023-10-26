from django.utils import translation

from apps.contrib.translations import get_search_fields


def test_get_search_fields():
    with translation.override("en"):
        fields = get_search_fields(["body", "page_title"])
        assert all(map(lambda field: field.endswith("_en"), fields))
    with translation.override("de"):
        fields = get_search_fields(["body", "page_title"])
        assert all(map(lambda field: field.endswith("_de"), fields))
    with translation.override("de_ls"):
        fields = get_search_fields(["body", "page_title"])
        assert all(map(lambda field: field.endswith("_de-ls"),
                       fields))
