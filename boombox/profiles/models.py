from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to="avatars/")

    def __unicode__(self):
        return u"%s" % self.user


class Post(models.Model):
    PROVIDERS = (
        ('youtube', 'Youtube'),
        ('kwejk', 'Kwejk'),
    )
    title = models.CharField(max_length=30)
    link = models.URLField()
    provider = models.CharField(max_length=20, choices=PROVIDERS)
    author = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return u"%s by %s" % (self.title, self.author)
