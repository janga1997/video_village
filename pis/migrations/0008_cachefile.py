# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-23 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pis', '0007_pi_ssh_tunnel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CacheFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('pi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pis.Pi')),
            ],
        ),
    ]
