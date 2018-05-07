# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.


class Goal(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    description = models.TextField(_('Description'))
    start_date = models.DateTimeField(_('Start Date'), null=True, blank=True)
    compliance_date = models.DateTimeField(_('Compliance Date'), null=True, blank=True)

    def __str__(self):
        return self.name
