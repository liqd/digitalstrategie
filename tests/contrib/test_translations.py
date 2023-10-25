from django.utils import translation

from apps.contrib.translations import get_search_fields


def test_get_search_fields():
    with translation.override("en"):
        fields = get_search_fields()
        assert all(map(lambda field: field.endswith("_en_edgengrams"), fields))
    with translation.override("de"):
        fields = get_search_fields()
        assert all(map(lambda field: field.endswith("_de_edgengrams"), fields))
    with translation.override("de_ls"):
        fields = get_search_fields()
        assert all(map(lambda field: field.endswith("_de-ls_edgengrams"),
                       fields))
