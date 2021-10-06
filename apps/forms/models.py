from django.db import models
from django.utils.translation import ugettext_lazy as _
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.edit_handlers import FieldRowPanel
from wagtail.admin.edit_handlers import MultiFieldPanel
from wagtail.admin.edit_handlers import ObjectList
from wagtail.admin.edit_handlers import TabbedInterface
from wagtail.contrib.forms.models import AbstractEmailForm
from wagtail.contrib.forms.models import AbstractFormField

from apps.contrib.translations import TranslatedField
from apps.settings import helpers


class FormField(AbstractFormField):
    page = ParentalKey('FormPage',
                       on_delete=models.CASCADE,
                       related_name='form_fields')


class FormPage(AbstractEmailForm):
    header_de = models.CharField(
        max_length=500, blank=True, verbose_name="Header")
    header_en = models.CharField(
        max_length=500, blank=True, verbose_name="Header")

    header_de_ls = models.CharField(
        max_length=500, blank=True, verbose_name="Header")

    thank_you_text_de = models.TextField()
    thank_you_text_en = models.TextField(blank=True)
    thank_you_text_de_ls = models.TextField(blank=True)

    header = TranslatedField(
        'header_de',
        'header_en',
        'header_de_ls',
    )

    thank_you_text = TranslatedField(
        'thank_you_text_de',
        'thank_you_text_en',
        'thank_you_text_de_ls',
    )

    def get_form_fields(self):
        fields = list(super().get_form_fields())

        fields.append(FormField(
            label='firstname',
            clean_name='firstname',
            help_text=_('First Name'),
            field_type='singleline',
            required=True))

        fields.append(FormField(
            label='surname',
            clean_name='surname',
            help_text=_('Surname'),
            field_type='singleline',
            required=True))

        fields.append(FormField(
            label='organisation',
            clean_name='organisation',
            help_text=_('Organisation'),
            field_type='singleline',
            required=False))

        fields.append(FormField(
            label='email',
            clean_name='email',
            help_text=_('E-Mail'),
            field_type='email',
            required=True))

        return fields

    en_content_panels = [
        FieldPanel('header_en'),
        FieldPanel('thank_you_text_en'),
    ]

    de_content_panels = [
        FieldPanel('header_de'),
        FieldPanel('thank_you_text_de'),
    ]

    de_ls_content_panels = [
        FieldPanel('header_de_ls'),
        FieldPanel('thank_you_text_de_ls'),
    ]

    common_panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    edit_handler = TabbedInterface([
        ObjectList(common_panels, heading='Common'),
        ObjectList(de_content_panels, heading='German'),
        ObjectList(en_content_panels, heading='English'),
        ObjectList(de_ls_content_panels, heading='Easy German')
    ])


class ContactFormPage(FormPage):

    def process_form_submission(self, form):
        form.fields.pop('data_protection')

        return super().process_form_submission(form)

    def get_form_fields(self):
        fields = list(super().get_form_fields())

        data_protection_help = _('I have read and accepted the {}data protection policy{}.')

        fields.insert(0, FormField(
            label='title',
            clean_name='title',
            help_text=_('Title'),
            field_type='singleline',
            required=False))

        fields.append(FormField(
            label='message',
            clean_name='message',
            help_text=_('Your message to us...'),
            field_type='multiline',
            required=True))

        fields.append(FormField(
            label='data_protection',
            clean_name='data_protection',
            field_type='checkbox',
            help_text=helpers.add_link_to_helptext(data_protection_help,
                                                   'data_protection_policy'),
            required=True))

        return fields

    def get_data_fields(self):
        data_fields = super().get_data_fields()
        # remove data_protection
        data_fields.pop()
        return data_fields
