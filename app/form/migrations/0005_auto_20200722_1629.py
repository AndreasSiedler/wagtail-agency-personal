# Generated by Django 3.0.8 on 2020-07-22 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('form', '0004_auto_20200722_1628'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formfield',
            options={},
        ),
        migrations.AddField(
            model_name='formfield',
            name='search_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image'),
        ),
    ]
