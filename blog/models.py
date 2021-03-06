# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField(default='Say\'n Hello!\nWaiting for new posts')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def __unicode__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
