from django.utils.translation import gettext_lazy as _
from wagtail import blocks
from wagtail.embeds import blocks as embed_blocks
from wagtail.images.blocks import ImageChooserBlock

HELPTEXT_RICHTEXT_A11Y = _('For accessibility please make sure that you do not'
                           ' leave out levels when using the headlines. That'
                           ' means, that there should always be an h2 before'
                           ' using an h3.')
NEWSLETTER_EMAIL_DEFAULT = _('Your email address')
NEWSLETTER_DSGVO_DEFAULT = _(
    'Ich willige in die Speicherung und Nutzung meiner E-Mail-Adresse für '
    'den Newsletterversand ein. Die Einwilligung gilt für den Zeitraum des '
    'Abonnements und kann jederzeit über den Link „Abmelden“ widerrufen '
    'werden. Die Datenschutzerklärung habe ich zur Kenntnis genommen.')


class ColorChoiceBlock(blocks.ChoiceBlock):
    choices = [
        ('yellow', 'Yellow'),
        ('pink', 'Pink'),
        ('purple', 'Purple'),
        ('green', 'Green')
    ]


class AccordionItemBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=130,
        verbose_name='FAQ Question'
    )
    body = blocks.RichTextBlock(
        required=False,
        verbose_name='FAQ Answer',
        help_text=HELPTEXT_RICHTEXT_A11Y
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
    quote = blocks.CharBlock(
        required=True
    )
    author = blocks.CharBlock(
        required=False
    )

    class Meta:
        label = _('Testimonial')
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
        help_text=_('How should the image be aligned?')
    )

    class Meta:
        template = 'apps_home/blocks/text_with_image_block.html'
        icon = 'image'


class ParagraphBlock(blocks.StructBlock):
    body = blocks.RichTextBlock(
        required=True,
        help_text=HELPTEXT_RICHTEXT_A11Y
    )

    class Meta:
        template = 'apps_home/blocks/paragraph_block.html'
        icon = 'doc-full'


class ThesisBlock(blocks.StructBlock):
    thesis = blocks.CharBlock(max_length=255, label=_('One thesis'))

    class Meta:
        template = 'apps_home/blocks/thesis_block.html'
        icon = 'pick'


class ThesisListBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    theses = blocks.ListBlock(
        ThesisBlock,
        label='All theses'
    )
    background_color = blocks.ChoiceBlock(
        help_text=_('Not choosing a colour will result in a '
                    'block with a white background.'),
        required=False,
        choices=[
            ('yellow', 'Yellow'),
            ('pink', 'Pink'),
            ('purple', 'Purple')
        ]
    )

    class Meta:
        template = 'apps_home/blocks/thesis_list_block.html'
        icon = 'list-ul'


# Teaser blocks
class TeaserBlockCentered(blocks.StructBlock):
    title = blocks.CharBlock(max_length=130)
    body = blocks.TextBlock(max_length=300, blank=True, rows=3)
    link = blocks.PageChooserBlock()
    link_text = blocks.CharBlock(max_length=50, label='Link Text')
    link_description = blocks.TextBlock(
        max_length=70,
        label=_('Link Description'),
        help_text=_('describe link for assistive technology if needed'),
        required=False
    )
    background_color = ColorChoiceBlock(
        help_text=_('Not choosing a colour will result in a '
                    'block with a white background.'),
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/teaser_block_centered.html'
        icon = 'arrow-down'


class TeaserBlockImage(blocks.StructBlock):
    title = blocks.CharBlock(max_length=130)
    body = blocks.TextBlock(max_length=630, blank=True, rows=3)
    image = ImageChooserBlock()
    link = blocks.PageChooserBlock()
    link_text = blocks.CharBlock(max_length=50, label='Link Text')
    link_description = blocks.TextBlock(
        max_length=70,
        label=_('Link Description'),
        help_text=_('describe link for assistive technology if needed'),
        required=False
    )

    background_color = ColorChoiceBlock(
        help_text=_('Not choosing a colour will result in a block with '
                    'a white background.'),
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
    link_description = blocks.TextBlock(
        max_length=70,
        label=_('Link Description'),
        help_text=_('describe link for assistive technology if needed'),
        required=False
    )


# sub-block
class ImgTextLinkBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock(max_length=130)
    body = blocks.TextBlock(max_length=500, blank=True, rows=3)
    button = LinkBlock(
        help_text=_('Add either an external or internal link, not both')
    )


# 2-3 column block with image and CTA
class TeaserBlockColumn(blocks.StructBlock):
    title = blocks.CharBlock(max_length=130)
    column_count = blocks.ChoiceBlock(choices=[
        ('2', 'two columns'),
        ('3', 'three columns')
    ], icon='cup', required=True,
        help_text=_('Only add this number of columns below'))
    column = blocks.ListBlock(ImgTextLinkBlock())

    class Meta:
        template = 'apps_home/blocks/teaser_block_columns.html'
        icon = 'grip'
        label = _('Teaser Columns')


class IconTextLinkBlock(blocks.StructBlock):
    icon = ImageChooserBlock()
    title = blocks.CharBlock(max_length=70)
    link = blocks.PageChooserBlock()
    link_description = blocks.TextBlock(
        max_length=70,
        label=_('Link Description'),
        help_text=_('describe link for assistive technology if needed'),
        required=False
    )


# tile teaser block with icon
class TeaserBlockTile(blocks.StructBlock):
    title = blocks.CharBlock(max_length=70)
    tile = blocks.ListBlock(IconTextLinkBlock())

    class Meta:
        template = 'apps_home/blocks/teaser_block_tiles.html'
        icon = 'pick'
        label = _('Icon Tiles')


class TeaserBlockSingle(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock(max_length=130)
    body = blocks.TextBlock(max_length=500)
    link = LinkBlock(
        help_text=_('Add either an external or internal link, not both')
    )

    class Meta:
        template = 'apps_home/blocks/teaser_block_single.html'
        icon = 'pick'
        label = _('Teaser Single')


class NewsletterBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=150)
    email_field_label = blocks.CharBlock(
        max_length=130,
        required=True,
        default=NEWSLETTER_EMAIL_DEFAULT
    )
    dsgvo_checkbox_label = blocks.CharBlock(
        max_length=500,
        required=True,
        default=NEWSLETTER_DSGVO_DEFAULT
    )
    background_color = ColorChoiceBlock(
        help_text=_('Not choosing a colour will result in a '
                    'block with a white background.'),
        required=False
    )

    class Meta:
        template = 'apps_home/blocks/newsletter_block.html'
        icon = 'mail'
        help_text = _('This form only works with sendinblue')


class VideoBlock(blocks.StructBlock):

    title = blocks.CharBlock(max_length=130, required=False)
    caption = blocks.CharBlock(
        max_length=255,
        required=False,
        help_text=_('Please insert a short description of the video '
                    '(character limit 255).'))
    video = embed_blocks.EmbedBlock(help_text=_('You can only add links to '
                                    'YouTube or Vimeo videos.'))
    preview_image = ImageChooserBlock(
        required=False,
        help_text=_('Add a preview image for the GDPR overlay.'))
    transcript = blocks.RichTextBlock(features=['bold', 'italic', 'ol', 'ul',
                                                'link', 'document-link'],
                                      help_text=_('You can add the video\'s '
                                                  'transcript here (unlimited '
                                                  'characters).'),
                                      required=False)

    class Meta:
        template = 'apps_home/blocks/video_block.html'
        icon = 'placeholder'
        label = _('Video Block')


class ImageSwiperBlock(blocks.StructBlock):
    class CustomImgTextLinkBlock(ImgTextLinkBlock):
        title = blocks.CharBlock(max_length=80)  # Set a new max_length
        body = blocks.TextBlock(max_length=200, blank=True, rows=3)
    swiper_item = blocks.ListBlock(
        CustomImgTextLinkBlock(
            help_text=_('Please note that images will be displayed in a 16:9 '
                        'aspect ratio. Crop or resize your images accordingly '
                        'before uploading to ensure they display correctly.')))

    class Meta:
        template = 'apps_home/blocks/image_swiper_block.html'
        icon = 'arrow-down'
