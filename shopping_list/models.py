from django.db import models
# from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True, default=0)
    checked_off = models.BooleanField(default=False)

    class Meta:
        ordering = ['checked_off', 'name']

    def __str__(self):
        return self.name


class List(models.Model):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(Item)
    created_on = models.DateTimeField('created on', auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    budget = models.IntegerField(default=0)

    def was_created_recently(self):
        return self.created_on >= timezone.now()

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.name
