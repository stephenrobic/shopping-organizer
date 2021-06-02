from django.db import models
# from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(blank=True)
    checked_off = models.BooleanField(default=False)

    class Meta:
        ordering = ['checked_off', 'name']


class List(models.Model):
    name = models.CharField(max_length=200)
    items = models.ManyToManyField(Item)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    budget = models.IntegerField(default=0)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.name
