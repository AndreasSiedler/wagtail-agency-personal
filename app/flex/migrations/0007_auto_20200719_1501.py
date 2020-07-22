# Generated by Django 3.0.8 on 2020-07-19 15:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0006_auto_20200719_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('person', wagtail.core.blocks.StructBlock([('first_name', wagtail.core.blocks.CharBlock()), ('surname', wagtail.core.blocks.CharBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('biography', wagtail.core.blocks.RichTextBlock())], icon='user')), ('carousel', wagtail.core.blocks.StreamBlock([('columns', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quotation', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.CharBlock())])), ('video', wagtail.embeds.blocks.EmbedBlock())], icon='cogs'))]),
        ),
    ]
