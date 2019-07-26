# Generated by Django 2.2.3 on 2019-07-21 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0002_auto_20190721_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stages_to_group', to='organization.Groups'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stages_to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]