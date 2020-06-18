"""Streamfields live in here"""

from wagtail.core import blocks

class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add yout title')
    text = blocks.TextBlock(required=True, help_text='Add additional Text')

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class ImageAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Add yout title')
    text = blocks.TextBlock(required=True, help_text='Add additional Text')

    class Meta:
        template = "streams/image_and_text_block.html"
        icon = "edit"
        label = "Image & Text"
