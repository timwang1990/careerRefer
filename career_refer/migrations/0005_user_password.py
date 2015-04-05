# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('career_refer', '0004_auto_20150404_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=datetime.datetime(2015, 4, 4, 18, 17, 21, 752787, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
