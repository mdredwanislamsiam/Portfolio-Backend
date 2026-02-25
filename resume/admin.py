from django.contrib import admin
from resume.models import Education, Experience, Skill
# Register your models here.
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)