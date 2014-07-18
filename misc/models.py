import datetime
from django.contrib.auth.models import User
from django.db import models

PROVIDERS = (
    ("YT", "Youtube"),
    ("SC", "SoundCloud"),
    # ("WR", "Wrzuta"),
    ("VI", "Vimeo"),
)


class Tag(models.Model):
    name = models.CharField(max_length=32, unique=True)
    count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Link(models.Model):
    title = models.CharField(max_length=100, blank=True)
    url = models.URLField(blank=True)
    submitted_on = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    author = models.ForeignKey(User)
    provider = models.CharField(max_length=2, choices=PROVIDERS,
                                default=PROVIDERS[0])
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        super(Link, self).save(*args, **kwargs)
        print(self.tags)

    def __unicode__(self):
        return "%s by %s" % (self.title, self.author)