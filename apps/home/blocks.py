from wagtail.core import blocks


class ColorChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('yellow', 'Yellow'),
        ('pink', 'Pink'),
        ('purple', 'Purple')
    ]


class CallToActionBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    body = blocks.RichTextBlock(
        required=True
    )
    link = blocks.PageChooserBlock(required=False)
    link_text = blocks.CharBlock(max_length=50, label='Link Text')
    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a CTA '
                  'block with a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/cta_block.html'
        icon = 'plus-inverse'


class AccordionItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        verbose_name='FAQ Question'
    )
    body = blocks.RichTextBlock(
        required=False,
        verbose_name='FAQ Answer'
    )


class FaqBlock(blocks.StructBlock):
    faq_title = blocks.CharBlock(
        required=False
    )
    accordion_items = blocks.ListBlock(AccordionItemBlock())
    background_color = ColorChoiceBlock(
        help_text=('Not choosing a colour will result in an FAQ block with '
                   'a white background.'),
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/faq_block.html'
        icon = 'arrow-down'


class QuoteBlock(blocks.StructBlock):
    text = blocks.RichTextBlock(
        required=True
    )
    quote = blocks.CharBlock(
        required=True
    )
    author = blocks.CharBlock(
        required=False
    )
    link = blocks.PageChooserBlock(
        required=False
    )
    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a Quote block with '
                  'a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/quote_block.html'
        icon = 'openquote'


class GruenbuchFaqBlock(blocks.StructBlock):
    faq_title = blocks.CharBlock(
        required=False
    )
    accordion_items = blocks.ListBlock(AccordionItemBlock())

    class Meta:
        template = 'apps_home/blocks/gruenbuch_faq_block.html'
        icon = 'arrow-down'
