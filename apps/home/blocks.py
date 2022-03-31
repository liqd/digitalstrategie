from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ColorChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('yellow', 'Yellow'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
        ('green', 'Green')
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
        max_length=130,
        verbose_name='FAQ Question'
    )
    body = blocks.RichTextBlock(
        required=False,
        verbose_name='FAQ Answer'
    )


class FaqBlock(blocks.StructBlock):
    faq_title = blocks.CharBlock(
        required=False,
        max_length=150
    )
    accordion_items = blocks.ListBlock(AccordionItemBlock())

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


class TextWithImageBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True)
    body = blocks.TextBlock(required=True, max_length=800)
    image = ImageChooserBlock(required=True)

    image_alignment = blocks.ChoiceBlock(
        choices=[
            ('left', 'left'),
            ('right', 'right'),
        ],
        icon='cup',
        default='left',
        help_text='How should the image be aligned?'
    )

    class Meta:
        template = 'apps_home/blocks/text_with_image_block.html'
        icon = 'image'


class CoulouredParagraphBlock(blocks.StructBlock):
    body = blocks.RichTextBlock(required=True)

    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a block with '
                  'a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/coloured_paragraph_block.html'
        icon = 'doc-full'


class ThesisBlock(blocks.StructBlock):
    thesis = blocks.CharBlock(max_length=255, label='One thesis')

    class Meta:
        template = 'apps_home/blocks/thesis_block.html'
        icon = 'pick'


class ThesisListBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    theses = blocks.ListBlock(
        ThesisBlock,
        label='All theses'
    )
    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a '
                  'block with a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/thesis_list_block.html'
        icon = 'list-ul'


# Teaser blocks
class TeaserBlockCentered(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50)
    body = blocks.TextBlock(max_length=300, blank=True, rows=3)
    link = blocks.PageChooserBlock()
    link_text = blocks.CharBlock(max_length=50, label='Link Text')
    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a '
                  'block with a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/teaser_block_centered.html'
        icon = 'arrow-down'


class TeaserBlockImage(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50)
    body = blocks.TextBlock(max_length=300, blank=True, rows=3)
    image = ImageChooserBlock()
    link = blocks.PageChooserBlock()
    link_text = blocks.CharBlock(max_length=50, label='Link Text')

    background_color = ColorChoiceBlock(
        help_text='Not choosing a colour will result in a block with '
                  'a white background.',
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/teaser_block_image.html'
        icon = 'image'


# sub-block
class LinkBlock(blocks.StructBlock):
    internal_link = blocks.PageChooserBlock(required=False)
    external_link = blocks.URLBlock(required=False)
    link_text = blocks.TextBlock(max_length=50, label='Link Text')


# sub-block
class ImgTextLinkBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock(max_length=50)
    body = blocks.TextBlock(max_length=500, blank=True, rows=3)
    button = LinkBlock(
        help_text='Add either an external or internal link, not both'
    )


# 2-3 column block with image and CTA
class TeaserBlockColumn(blocks.StructBlock):
    column_count = blocks.ChoiceBlock(choices=[
        ('2', 'two columns'),
        ('3', 'three columns')
    ], icon='cup', required=True,
        help_text='Only add this number of columns below')
    column = blocks.ListBlock(ImgTextLinkBlock())

    class Meta:
        template = 'apps_home/blocks/teaser_columns.html'
        icon = 'grip'
        label = 'Teaser Columns'


class IconTextLinkBlock(blocks.StructBlock):
    icon = ImageChooserBlock()
    title = blocks.CharBlock(max_length=70)
    link = blocks.PageChooserBlock(
        page_type=['apps_gruenbuch.GruenbuchDetailPage'])


# tile teaser block with icon
class TeaserBlockTile(blocks.StructBlock):
    title = blocks.CharBlock(max_length=70)
    tile = blocks.ListBlock(IconTextLinkBlock())

    class Meta:
        template = 'apps_home/blocks/teaser_block_tiles.html'
        icon = 'pick'
        label = 'Teaser Tiles'
