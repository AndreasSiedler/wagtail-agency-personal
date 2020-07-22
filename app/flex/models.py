from django.db import models
from django import forms

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel

from wagtail.images.blocks import ImageChooserBlock
from wagtail.core import blocks
from wagtail.embeds.blocks import EmbedBlock

from wagtailmetadata.models import MetadataPageMixin

# Create your models here.
class FlexPage(MetadataPageMixin, Page):
    intro = models.CharField(max_length=250, blank=True)
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('row', blocks.StructBlock([
            ('layout', blocks.MultipleChoiceBlock(choices=[
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
                ("test", "test2"),
            ], widget=forms.SelectMultiple)),
            ('carousel', blocks.StreamBlock(
                [
                    # ('columns', blocks.ListBlock([
                    #     ('column', blocks.CharBlock()),
                    # ])),
                    ('image', ImageChooserBlock()),
                    ('quotation', blocks.StructBlock([
                        ('text', blocks.TextBlock()),
                        ('author', blocks.CharBlock()),
                    ])),
                    ('video', EmbedBlock()),
                ],
                icon='cogs'
            ))
        ], icon='user')),

    ])

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('body'),
    ]
