# Generated by Django 5.1.4 on 2025-01-14 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_bestseller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestseller',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bestseller',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='bestseller',
            name='published_date',
        ),
    ]
