from django.contrib import admin
from models import Link, Tag, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model


class LinkAdmin(admin.ModelAdmin):
    list_display = ("title", "provider")

admin.site.register(Link, LinkAdmin)


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

admin.site.register(Tag, TagAdmin)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)

