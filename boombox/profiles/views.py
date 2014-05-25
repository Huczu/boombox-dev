# from django.shortcuts import render
# -*- coding: utf-8 -*-
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"Strona główna")


def show_profile(request):
    return HttpResponse(u"Pokaż profil osoby zalogowanej.")


def show_users(request):
    return HttpResponse(u"Pokaż listę użytkowników.")


def show_user(request, user_slug):
    return HttpResponse(u"Pokaż wybranego użytkownika: %s" % user_slug)
