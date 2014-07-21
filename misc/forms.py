# coding=utf-8
from django.forms import ModelForm
from models import UserProfile, Link
from django import forms


class UserProfileForm(ModelForm):
    class Meta(object):
        model = UserProfile
        exclude = ("user", )


class LinkForm(ModelForm):
    # tags = forms.CharField()

    class Meta(object):
        model = Link
        exclude = ("author", "slug", )
        # exclude = ("author", "tags", "slug", )
