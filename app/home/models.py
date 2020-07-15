from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

from wagtailmetadata.models import MetadataPageMixin


class HomePage(MetadataPageMixin, Page):
    """Home page model"""
    
    templates = "home/home_page.html"
    # There can only be one homepage instance at the time
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)

    content_panels = Page.content_panels +  [
        FieldPanel("banner_title")
    ]

    # class Meta:
    #     verbose_name = "Oh hello World"
    #     verbose_name_plural = "Plural Name"
