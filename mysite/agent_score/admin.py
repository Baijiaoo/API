# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

#class ScoreInline(admin.TabularInline):
    #model = Score
    #extra = 2

#class AgentAdmin(admin.ModelAdmin):
    #list_display =  ['id','name']
    #list_filter = ['name']
    #search_fields = ['name']
    #list_per_page = 1

    #inlines = [ScoreInline]

# Register your models here.
#admin.site.register(agent)#AgentAdmin)
#admin.site.register(Score)