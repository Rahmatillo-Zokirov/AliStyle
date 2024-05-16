# Generated by Django 5.0.6 on 2024-05-16 06:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_ichkibolim'),
    ]

    operations = [
        migrations.AddField(
            model_name='ichkibolim',
            name='bolim',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.bolim'),
        ),
        migrations.AlterField(
            model_name='ichkibolim',
            name='rasm',
            field=models.ImageField(upload_to='ichki-bolimlar/'),
        ),
    ]
