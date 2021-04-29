from django.db import models

from django.db import models
from django.db.models.signals import post_save, post_delete

from changelog.signals import journal_save_handler, journal_delete_handler

from changelog.mixins import ChangeloggableMixin
from institution.models import Institution



class Category(models.Model):
    slug = models.SlugField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='categories', blank=True, null=True)

    def __str__(self):
        return self.name







class Invent(ChangeloggableMixin,models.Model):
    title = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=15, unique=True)
    invent_number = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='invents', blank=True, null=True)
    description = models.TextField()
    institution = models.ForeignKey(Institution, related_name='institutions', null=True, on_delete=models.SET_NULL, blank=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='invents')
    act_number = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.title

post_save.connect(journal_save_handler, sender=Invent)
post_delete.connect(journal_delete_handler, sender=Invent)
