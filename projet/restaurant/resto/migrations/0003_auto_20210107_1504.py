# Generated by Django 3.0.8 on 2021-01-07 15:04

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Nos Services', 'verbose_name_plural': 'Nos Services'},
        ),
        migrations.CreateModel(
            name='VoirTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200)),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='resto.Voir')),
            ],
            options={
                'verbose_name': 'voir Translation',
                'db_table': 'resto_voir_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
