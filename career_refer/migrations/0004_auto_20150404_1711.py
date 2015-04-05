# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career_refer', '0003_auto_20150403_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('headImg', models.FileField(upload_to='./upload/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='employee',
            name='reporters',
            field=models.ManyToManyField(to='career_refer.Reporter'),
            preserve_default=True,
        ),
    ]
