# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='apodo',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='descripcion',
        ),
        migrations.AddField(
            model_name='post',
            name='nombre',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
