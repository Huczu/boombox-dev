# coding=utf-8
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

PROVIDERS = (
    ("YT", "Youtube"),
    ("SC", "SoundCloud"),
    ("VI", "Vimeo"),
)


class Tag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Tag, self).save(*args, **kwargs)


class Link(models.Model):
    """
    Klasa dodająca muzyczkę.
    """
    title = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    submitted_on = models.DateTimeField(auto_now_add=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, related_name='author')
    provider = models.CharField(max_length=2, choices=PROVIDERS,
                                default=PROVIDERS[0])
    slug = models.SlugField(null=True, unique=True)
    # tags = models.ManyToManyField(Tag)
    tags = TaggableManager()

    def __unicode__(self):
        return "%s by %s" % (self.title, self.author)

    def get_absolute_url(self):
        return reverse("link_detail",
                       kwargs={"slug": str(self.slug), "pk": str(self.pk)})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Link, self).save(*args, **kwargs)


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    about = models.TextField(max_length=200, null=True)
    avatar = models.ImageField(upload_to="media/avatars/",
                               default="default.jpg", null=True)
    friends = models.ManyToManyField(User, related_name='friends')


    def __unicode__(self):
        return "Profil %s" % self.user.username


def create_profile(**kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        up = UserProfile(user=user)
        up.save()


post_save.connect(create_profile, sender=User)
