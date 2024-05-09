# Generated by Django 5.0.4 on 2024-05-07 05:50

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('narx1', models.FloatField()),
                ('narx2', models.FloatField(blank=True, null=True)),
                ('miqdor', models.FloatField()),
                ('olchov', models.CharField(max_length=20)),
                ('sana', models.DateField(auto_now=True)),
                ('tarqatuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mahsulot',
                'verbose_name_plural': 'Mahsulotlar',
            },
        ),
        migrations.CreateModel(
            name='Mijoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('dokon', models.CharField(blank=True, max_length=100, null=True)),
                ('tel', models.CharField(max_length=14)),
                ('manzil', models.TextField(max_length=255)),
                ('qarz', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('oluvchi', models.CharField(max_length=20)),
                ('tarqatuvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Mijoz',
                'verbose_name_plural': 'Mijozlar',
            },
        ),
    ]
