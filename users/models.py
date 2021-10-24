from django.db import models
from django.contrib.auth.models import User


# Create your models here.
LESSONS  = [
    ('Mathematics','Matemati̇k'),
    ('Physics', 'Fi̇zi̇k'),
    ('Literature', 'Edebi̇yat'),
    ('Psychology', 'Pi̇skoloji̇'),
    ('Business', 'İşletme'),
    ('Philosophy', 'Felsefe'),
    ('Religion', 'Di̇n'),
]

class Note(models.Model):
    user_name = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    note = models.IntegerField()
    cover_image = models.ImageField(
        upload_to = 'note',
        null = True,
        blank = True,
    )
    lesson = models.CharField(
        choices=LESSONS,
        max_length=13,
        default=""
    )

