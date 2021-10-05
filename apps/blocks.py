from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ColorChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('yellow', 'Yellow'),
        ('pink', 'Pink'),
        ('purple', 'Purple')
    ]


class CallToActionBlock(blocks.StructBlock):
    body = blocks.RichTextBlock()
    link = blocks.CharBlock()
    link_text = blocks.CharBlock(max_length=50, label='Link Text')

    class Meta:
        template = 'apps_home/blocks/cta_block.html'
        icon = 'plus-inverse'


class ImageCallToActionBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock(max_length=80)
    body = blocks.RichTextBlock()
    link = blocks.CharBlock()
    link_text = blocks.CharBlock(max_length=50, label='Link Text')

    class Meta:
        template = 'apps_home/blocks/image_cta_block.html'
        icon = 'image'


class ColumnsBlock(blocks.StructBlock):
    columns_count = blocks.ChoiceBlock(choices=[
        (2, 'Two columns'),
        (3, 'Three columns'),
        (4, 'Four columns'),
        (6, 'Six columns')

    ], default=2)

    columns = blocks.ListBlock(
        blocks.RichTextBlock(label='Column body'),
    )

    class Meta:
        template = 'apps_home/blocks/columns_block.html'
        icon = 'grip'


class AccordionItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.RichTextBlock(required=False)


class FaqBlock(blocks.StructBlock):
    accordion_items = blocks.ListBlock(AccordionItemBlock())
    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in an FAQ block with a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/faq_block.html'
        icon = 'arrow-down'
