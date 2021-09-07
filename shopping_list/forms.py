# from django import forms
from django.forms import ModelForm
from shopping_list.models import List


class CreateListForm(ModelForm):
    class Meta:
        model = List
        fields = ['name', 'budget']
