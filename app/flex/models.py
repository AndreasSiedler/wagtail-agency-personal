""" Flex Page """

from wagtail.admin.edit_handlers import StreamFieldPanel, RichTextFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField, RichTextField
from wagtail.api import APIField

from .blocks import (LogoCloudBlock, PortfolioSectionBlock, TestimonialSectionBlock,
                     HeroSectionBlock, ContentSectionBlock, FeatureSectionBlock)


# Create your models here.


class FlexPage(Page):
    """
    Abstract Page Extension
    Define abstract to dont create own database table for this model - fields are created in the child class
    """
    seo_text = RichTextField(blank=True, null=True, verbose_name="SEO Text",)
    content = StreamField(
        [
            ('logo_cloud_section_block', LogoCloudBlock()),
            ('portfolio_section_block', PortfolioSectionBlock()),
            ('testimonial_section_block', TestimonialSectionBlock()),
            ('hero_section_block', HeroSectionBlock()),
            ('content_section_block', ContentSectionBlock()),
            ('feature_section_block', FeatureSectionBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        RichTextFieldPanel("seo_text"),
        StreamFieldPanel("content"),
    ]

    template = "flex/flex_page.html"

    class Meta:
        abstract = True
