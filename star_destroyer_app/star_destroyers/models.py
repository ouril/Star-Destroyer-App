import uuid

from django.db import models


def make_upload_path(instance, filename, prefix=False):
    """Create unqiue name for Image
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    index = parts[-1]
    filename = new_name + '.' + index
    return filename


# Create your models here.
class StarDestroyer(models.Model):
    VICTORY = 'Victory'
    EMERIAL = 'Emperial'
    TYPES = [
        (VICTORY, 'Victory'),
        (EMERIAL, 'Emperial')
    ]
    name = models.CharField(
        max_length=40,
        verbose_name='Name',
        unique=True
    )
    capitane = models.CharField(
        max_length=40,
        verbose_name='Capitan',
        unique=True
    )
    typeof = models.CharField(
        max_length=7,
        choices=TYPES,
        verbose_name='Type of star destroyer'
    )
    number_of_people = models.PositiveIntegerField(default=400)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to=make_upload_path,
        default='',
        blank=True
    )

    def __str__(self):
        return 'StarDestroyer class ' + self.typeof + ' ' + self.name