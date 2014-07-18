from django.views.generic import ListView, DetailView
from misc.models import Link, Tag


class LatestLinkView(ListView):
    model = Link
    queryset = Link.objects.all().order_by('-submitted_on')
    paginate_by = 5
    template_name = "misc/latest_link_list.html"


class TagView(ListView):
    model = Tag
    template_name = "misc/tag_list.html"


class TagDetailView(DetailView):
    model = Tag