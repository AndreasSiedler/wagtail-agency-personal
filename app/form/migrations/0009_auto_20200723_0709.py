# Generated by Django 3.0.8 on 2020-07-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_formpage_button_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formpage',
            name='button_text',
            field=models.CharField(default='Anfrage senden', max_length=50),
        ),
    ]
