# Generated by Django 3.1 on 2021-04-13 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories')),
            ],
        ),
        migrations.CreateModel(
            name='Invent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('serial_number', models.CharField(max_length=15, unique=True)),
                ('invent_number', models.CharField(max_length=15, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='invents')),
                ('description', models.TextField()),
                ('act_number', models.IntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invents', to='main.category')),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institutions', to='institution.institution')),
            ],
        ),
    ]
