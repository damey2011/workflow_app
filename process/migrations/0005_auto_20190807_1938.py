# Generated by Django 2.2.3 on 2019-08-07 19:38

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0004_auto_20190807_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='formresponse',
            name='fb_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
        migrations.CreateModel(
            name='FormResponseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('field_name', models.CharField(max_length=500)),
                ('file', models.FileField(upload_to='form-responses/')),
                ('form_response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process.Formresponse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]