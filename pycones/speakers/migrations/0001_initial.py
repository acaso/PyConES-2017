# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 12:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markupfield.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Tal como quieres que apareza en el programa de la conferencia.', max_length=100, verbose_name='Nombre')),
                ('biography', markupfield.fields.MarkupField(blank=True, default='', help_text="Unas palabras sobre ti. Edita usando <a href='http://warpedvisions.org/projects/markdown-cheat-sheet/target='_blank'>Markdown</a>.", rendered_field=True, verbose_name='Biografía')),
                ('biography_markup_type', models.CharField(choices=[('', '--'), ('markdown', 'markdown')], default='markdown', max_length=30)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='speakers', verbose_name='Foto')),
                ('_biography_rendered', models.TextField(editable=False)),
                ('annotation', models.TextField(blank=True, default='')),
                ('is_keynoter', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='speaker', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]