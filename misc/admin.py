from django.contrib import admin
from models import Link, Tag


class LinkAdmin(admin.ModelAdmin):
    list_display = ("title", "provider", "author", )

admin.site.register(Link, LinkAdmin)


class TagAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)