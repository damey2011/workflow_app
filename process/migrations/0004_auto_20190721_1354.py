# Generated by Django 2.2.3 on 2019-07-21 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('process', '0003_auto_20190721_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='createdstage', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='createdtask', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
