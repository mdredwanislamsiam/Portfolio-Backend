from django.contrib import admin
from research.models import Research, ResearchDomain, Conference

admin.site.register(Research)
admin.site.register(ResearchDomain)
admin.site.register(Conference)