# Generated by Django 3.2.8 on 2021-10-24 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='note'),
        ),
    ]
