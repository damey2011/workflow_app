# Generated by Django 2.2.3 on 2019-07-21 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('file', models.CharField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orgdocuments', to='organization.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userdocuments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('form_name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('fields', models.TextField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orgforms', to='organization.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userforms', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Formresponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('response', models.TextField(max_length=255)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='formresponse', to='process.Form')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userformresponse', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('process_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=255)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='processorg', to='organization.Organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdprocesses', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('order', models.CharField(max_length=255)),
                ('groups', models.CharField(max_length=255, null=True)),
                ('users', models.CharField(max_length=255, null=True)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stages', to='process.Process')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='documenttasks', to='process.Document')),
                ('form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='formtasks', to='process.Form')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='process.Stage')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
