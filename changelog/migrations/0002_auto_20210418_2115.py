# Generated by Django 3.1 on 2021-04-18 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('changelog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='changelog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор изменения'),
        ),
    ]
