# Generated by Django 4.2.7 on 2024-05-14 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['id'], 'verbose_name_plural': 'entries'},
        ),
    ]
