"""Streamfields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add yout title')
    text = blocks.TextBlock(required=True, help_text='Add additional Text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=True, help_text='Choose an image')
    title = blocks.CharBlock(required=True, help_text='Add yout title')
    text = blocks.TextBlock(required=True, help_text='Add additional Text')

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "edit"
        label = "Image & Text"


class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full Rich Text"


class SimpleRichTextBlock(blocks.RichTextBlock):
    """RichtextField without (limited) all the features """
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        # call the super and then override features
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple Rich Text"
