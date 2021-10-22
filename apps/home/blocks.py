from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


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
        help_text='Not choosing a colour will result in a '
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
        help_text=('Not choosing a colour will result in a block with '
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
        help_text='Not choosing a colour will result in a block with '
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


class TextWithImageBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=True)
    image = ImageChooserBlock(required=True)

    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a block with '
                  'a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/text_with_image_block.html'
        icon = 'arrow-down'


# teaser blocks

class TeaserBlockCentered(blocks.StructBlock):

    link = blocks.PageChooserBlock(
        target_model=['apps_home.DetailPage',
                      'apps_gruenbuch.GruenbuchIndexPage'],
        help_text='Make sure that teaser title and teaser intro '
                  'of the chosen page are set.'
    )
    link_text = blocks.CharBlock(max_length=50, label='Link Text')
    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a '
                  'block with a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/teaser_block_centered.html'
        icon = 'arrow-down'


class TeaserBlockTwoColumns(blocks.StructBlock):

    link_1 = blocks.PageChooserBlock(
        target_model=['apps_home.DetailPage',
                      'apps_gruenbuch.GruenbuchIndexPage'],
        help_text='Make sure that teaser title and teaser intro '
                  'of the chosen page are set.'
    )
    link_1_text = blocks.CharBlock(max_length=50, label='Link Text')

    link_2 = blocks.PageChooserBlock(
        target_model=['apps_home.DetailPage',
                      'apps_gruenbuch.GruenbuchIndexPage'],
        help_text='Make sure that teaser title and teaser intro '
                  'of the chosen page are set.'
    )
    link_2_text = blocks.CharBlock(max_length=50, label='Link Text')

    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a '
                  'block with a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/teaser_block_two_columns.html'
        icon = 'arrow-down'


class TeaserBlockImageLeft(blocks.StructBlock):

    link = blocks.PageChooserBlock(
        target_model=['apps_home.DetailPage',
                      'apps_gruenbuch.GruenbuchIndexPage'],
        help_text='Make sure that teaser title, teaser intro and teaser image '
                  'of the chosen page are set.'
    )
    link_text = blocks.CharBlock(max_length=50, label='Link Text')
    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a '
                  'block with a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/teaser_image_left.html'
        icon = 'image'


class TeaserBlockImageRight(blocks.StructBlock):

    link = blocks.PageChooserBlock(
        target_model=['apps_home.DetailPage',
                      'apps_gruenbuch.GruenbuchIndexPage'],
        help_text='Make sure that teaser title, teaser intro and teaser image '
                  'of the chosen page are set.'
    )
    link_text = blocks.CharBlock(max_length=50, label='Link Text')
    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a '
                  'block with a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/teaser_image_right.html'
        icon = 'image'
