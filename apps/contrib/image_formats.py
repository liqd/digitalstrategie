# image_formats.py
from wagtail.images.formats import Format
from wagtail.images.formats import register_image_format

register_image_format(
    Format(
        "image_960", "Full Width Optimised", "richtext-image full-width",
        "width-960"
    )
)
