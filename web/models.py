from __future__ import unicode_literals

from django.db import models

HOST_TYPES = (
    ('H', 'Hotel'),
    ('A', 'Alquiler vacacional'),
    ('B', 'B&B'),
    ('O', 'Otros'),
)

SCORES = (
    ('1', '1 de 5'),
    ('1,5', '1,5 de 5'),
    ('2', '2 de 5'),
    ('2,5', '2,5 de 5'),
    ('3', '3 de 5'),
    ('3,5', '3,5 de 5'),
    ('4', '4 de 5'),
    ('4,5', '4,5 de 5'),
    ('5', '5 de 5'),
)


# Create your models here.
class Host(models.Model):

    type = models.CharField(max_length=1, choices=HOST_TYPES, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    total = models.CharField(max_length=3, choices=SCORES, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

    class meta:
        pass
