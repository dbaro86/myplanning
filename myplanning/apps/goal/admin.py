# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Goal
# Register your models here.


class GoalAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'start_date', 'compliance_date']

admin.site.register(Goal, GoalAdmin)