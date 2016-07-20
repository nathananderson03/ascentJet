# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0003_auto_20141201_0851'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='node',
            name='slug',
            field=django_autoslug.fields.AutoSlugField(recursive=b'\'"\\\'parent\\\'"\'', populate_from=b'\'"(\\\'name\\\',)"\'', editable=False, use_recursive_slug=b'"\'True\'"', max_length=255, separator=b'\'"u\\\'-\\\'"\'', blank=True, unique=True, verbose_name='slug', overwrite=b'"\'False\'"'),
            preserve_default=True,
        ),
    ]
