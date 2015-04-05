# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career_refer', '0005_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='headImg',
        ),
    ]
