from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Chat(models.Model):
    user = models.ForeignKey(User)
    message = models.CharField(max_length=1000)
    time_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.message