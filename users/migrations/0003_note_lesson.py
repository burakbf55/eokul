# Generated by Django 3.2.8 on 2021-10-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_note_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='lesson',
            field=models.CharField(choices=[('Mathematics', 'Matemati̇k'), ('Physics', 'Fi̇zi̇k'), ('Literature', 'Edebi̇yat'), ('Psychology', 'Pi̇skoloji̇'), ('Business', 'İşletme'), ('Philosophy', 'Felsefe'), ('Religion', 'Di̇n')], default='', max_length=13),
        ),
    ]
