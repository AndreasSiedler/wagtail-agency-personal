""" All blocks """
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.blocks import PageChooserBlock


# Hero Section Block
class HeroSectionBlock(blocks.StructBlock):
    """ Section Base Block - Ued by each section """
    heading = blocks.CharBlock(
        required=False,
        max_length=80,
        label='Heading',
        default='Super Awesome Feature',
    )
    subheading = blocks.CharBlock(
        required=False,
        max_length=100,
        label='Subheading',
        default='Super Awesome Hero Subheading',
    )
    description = blocks.TextBlock(
        required=False,
        max_length=400,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )
    button = blocks.CharBlock(
        required=False,
        max_length=100,
        label='Button text',
        default='Get in touch',
    )
    page_link = PageChooserBlock(
        required=False,
        label='Page link'
    )
    image = ImageChooserBlock(
        required=False,
        label='Image',
        width='fill-960x720'
    )

    class Meta:
        """ Meta data """
        template = 'blocks/hero_section.html'
        label = 'Hero Section'



# Content Seciton Block
class ContentSectionBlock(blocks.StructBlock):
    """ Section Base Block - Ued by each section """
    layout = blocks.ChoiceBlock(
        choices=(
            ('centered', 'Centered'),
            ('two_columns_with_image', 'Two columns with image')
        )
    )
    heading = blocks.CharBlock(
        required=False,
        max_length=80,
        label='Heading',
        default='Super Awesome Section',
    )
    content = blocks.RichTextBlock(
        required=False,
        max_length=10000,
        label='Content',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )

    class Meta:
        """ Meta data """
        template = 'blocks/content_section.html'
        label = 'Content Section'


# Blog Section
class PortfolioSectionBlock(blocks.StructBlock):
    """ Blog Section Block """
    custom_classes = blocks.CharBlock(
        required=False,
        max_length=100,
        label="Classes"
    )
    heading = blocks.CharBlock(
        required=False,
        max_length=100,
        label="Heading"
    )
    description = blocks.TextBlock(
        required=False,
        max_length=400,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )
    projects = blocks.ListBlock(
        blocks.StructBlock([
            ("title", blocks.CharBlock(required=True, max_length=100)),
            ("description", blocks.CharBlock(required=True, max_length=200)),
            ("image", ImageChooserBlock(required=True, label="Image")),
            ("link", blocks.URLBlock(required=True, max_length=100)),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/portfolio_section.html'
        label = 'Portfolio Section'


# Testimonial Section Block
class TestimonialSectionBlock(blocks.StructBlock):
    """ Testimonial Section Block  """
    heading = blocks.CharBlock(
        required=False,
        max_length=80,
        label='Feature',
        default='Super Awesome Feature',
    )
    subheading = blocks.CharBlock(
        required=False,
        max_length=100,
        label='Subheading',
        default='Super Awesome Hero Subheading',
    )
    description = blocks.TextBlock(
        required=False,
        max_length=400,
        label='Description',
        default='The thing we do is better than any other similar thing and this hero panel will convince you of that, just by having a glorious background image.',
    )
    testimonials = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=False, label="Image")),
            ("name", blocks.CharBlock(required=False, max_length=100)),
            ("category", blocks.CharBlock(required=False, max_length=100)),
            ("content", blocks.TextBlock(required=True, max_length=300)),
        ])
    )

    class Meta:
        """ Meta data """
        template = 'blocks/testimonial_section.html'
        label = 'Testimonial Section'


# Logo Cloud Blocks

class LogoCloudBlock(blocks.StructBlock):
    """ LogoCloud Block """
    logos = blocks.ListBlock(
        blocks.StructBlock([
            ("image", ImageChooserBlock(required=True, label="Image")),
        ])
    )

    class Meta:
        """ Meta data """
        template = 'blocks/logo_cloud_section.html'
        label = 'Logo Cloud'


# Feature Section Block

class FeatureSectionBlock(blocks.StructBlock):
    """ Feature Section Block """
    heading = blocks.CharBlock(required=True, max_length=100, label="Title")
    features = blocks.ListBlock(
        blocks.StructBlock([
            ("icon", blocks.RawHTMLBlock(required=True, rows=5)),
            ("heading", blocks.CharBlock(required=True, max_length=100)),
            ("description", blocks.TextBlock(required=True, max_length=300)),
        ])
    )

    class Meta:
        """ meta data """
        template = 'blocks/feature_section.html'
        label = 'Feature Section'
