# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-16 19:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160513_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paginas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagina', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
