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


class AccordionItemBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.RichTextBlock(required=False)


class FaqBlock(blocks.StructBlock):
    accordion_items = blocks.ListBlock(AccordionItemBlock())
    background_color = ColorChoiceBlock(
        help_text=('Not choosing a colour will result in an FAQ block with '
                   'a white background.'),
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/faq_block.html'
        icon = 'arrow-down'
