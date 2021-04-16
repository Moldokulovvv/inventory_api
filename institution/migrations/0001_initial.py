# Generated by Django 3.1 on 2021-04-13 08:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Oblast',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='institution')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institutions', to='institution.address')),
                ('oblast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oblasti', to='institution.oblast')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='oblast',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oblasts', to='institution.oblast'),
        ),
        migrations.AddField(
            model_name='address',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='institution.address'),
        ),
    ]