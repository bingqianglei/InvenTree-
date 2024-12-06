# Generated by Django 4.2.16 on 2024-11-24 12:41

import django.db.models.deletion
from django.db import migrations, models

import InvenTree.models


class Migration(migrations.Migration):
    dependencies = [
        ('plugin', '0009_alter_pluginconfig_key'),
        ('common', '0031_auto_20241026_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectionList',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'metadata',
                    models.JSONField(
                        blank=True,
                        help_text='JSON metadata field, for use by external plugins',
                        null=True,
                        verbose_name='Plugin Metadata',
                    ),
                ),
                (
                    'name',
                    models.CharField(
                        help_text='Name of the selection list',
                        max_length=100,
                        unique=True,
                        verbose_name='Name',
                    ),
                ),
                (
                    'description',
                    models.CharField(
                        blank=True,
                        help_text='Description of the selection list',
                        max_length=250,
                        verbose_name='Description',
                    ),
                ),
                (
                    'locked',
                    models.BooleanField(
                        default=False,
                        help_text='Is this selection list locked?',
                        verbose_name='Locked',
                    ),
                ),
                (
                    'active',
                    models.BooleanField(
                        default=True,
                        help_text='Can this selection list be used?',
                        verbose_name='Active',
                    ),
                ),
                (
                    'source_string',
                    models.CharField(
                        blank=True,
                        help_text='Optional string identifying the source used for this list',
                        max_length=1000,
                        verbose_name='Source String',
                    ),
                ),
                (
                    'created',
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text='Date and time that the selection list was created',
                        verbose_name='Created',
                    ),
                ),
                (
                    'last_updated',
                    models.DateTimeField(
                        auto_now=True,
                        help_text='Date and time that the selection list was last updated',
                        verbose_name='Last Updated',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Selection List',
                'verbose_name_plural': 'Selection Lists',
            },
            bases=(InvenTree.models.PluginValidationMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SelectionListEntry',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'value',
                    models.CharField(
                        help_text='Value of the selection list entry',
                        max_length=255,
                        verbose_name='Value',
                    ),
                ),
                (
                    'label',
                    models.CharField(
                        help_text='Label for the selection list entry',
                        max_length=255,
                        verbose_name='Label',
                    ),
                ),
                (
                    'description',
                    models.CharField(
                        blank=True,
                        help_text='Description of the selection list entry',
                        max_length=250,
                        verbose_name='Description',
                    ),
                ),
                (
                    'active',
                    models.BooleanField(
                        default=True,
                        help_text='Is this selection list entry active?',
                        verbose_name='Active',
                    ),
                ),
                (
                    'list',
                    models.ForeignKey(
                        blank=True,
                        help_text='Selection list to which this entry belongs',
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='entries',
                        to='common.selectionlist',
                        verbose_name='Selection List',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Selection List Entry',
                'verbose_name_plural': 'Selection List Entries',
                'unique_together': {('list', 'value')},
            },
        ),
        migrations.AddField(
            model_name='selectionlist',
            name='default',
            field=models.ForeignKey(
                blank=True,
                help_text='Default entry for this selection list',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='common.selectionlistentry',
                verbose_name='Default Entry',
            ),
        ),
        migrations.AddField(
            model_name='selectionlist',
            name='source_plugin',
            field=models.ForeignKey(
                blank=True,
                help_text='Plugin which provides the selection list',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='plugin.pluginconfig',
                verbose_name='Source Plugin',
            ),
        ),
    ]