# from django import forms
from django.forms import ModelForm
from shopping_list.models import List
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CreateListForm(ModelForm):
    class Meta:
        model = List
        fields = ['name', 'budget']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # overide the init function
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # make the UserCreationForm username field have this form-control class, so it can be styled
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter username...'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter password...'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password...'})
