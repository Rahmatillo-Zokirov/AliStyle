# Generated by Django 5.0.6 on 2024-05-16 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IchkiBolim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('rasm', models.ImageField(upload_to='ichkibolim/')),
            ],
        ),
    ]
