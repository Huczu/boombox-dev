# coding=utf-8
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView, \
    DeleteView
from misc.forms import UserProfileForm, LinkForm
from misc.models import Link, UserProfile
from django.contrib.auth.models import User
from taggit.models import Tag
from django.contrib.auth import get_user_model


class LatestLinkView(ListView):
    model = Link
    queryset = Link.objects.all().order_by('-submitted_on')
    paginate_by = 2
    template_name = "misc/link_latest.html"


class CreateLinkView(CreateView):
    model = Link
    form_class = LinkForm
    template_name = "misc/link_create.html"

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        return super(CreateLinkView, self).form_valid(form)


class UpdateLinkView(UpdateView):
    model = Link
    form_class = LinkForm
    template_name = "misc/link_update.html"

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update stories """
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect(obj)
        return super(UpdateLinkView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        f = form.save(commit=False)
        f.author = self.request.user
        f.save()
        return super(UpdateView, self).form_valid(form)


class DeleteLinkView(DeleteView):
    model = Link
    success_url = reverse_lazy("latest")

    def dispatch(self, request, *args, **kwargs):
        """ Making sure that only authors can update stories """
        obj = self.get_object()
        if obj.author != self.request.user:
            return redirect(obj)
        return super(DeleteLinkView, self).dispatch(request, *args, **kwargs)



class DashboardView(ListView):
    model = Link
    template_name = "misc/link_latest.html"

    def get_queryset(self):
        queryset = Link.objects.all().filter(
            author_id=self.request.user.id).order_by('-submitted_on')
        return queryset


class TagsListView(ListView):
    model = Tag
    template_name = "misc/tag_list.html"


class UsersListView(ListView):
    model = User
    template_name = "misc/user_list.html"


class TagDetailView(DetailView):
    model = Tag
    template_name = "misc/tag_detail.html"


class LinkDetailView(DetailView):
    model = Link


class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "misc/user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user


class UserProfileEditView(UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = "misc/userprofile_update.html"

    def get_object(self, query=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

    def get_success_url(self):
        return reverse("profile", kwargs={"slug": self.request.user})

