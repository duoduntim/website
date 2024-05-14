from django.contrib import admin
from . models import Projects,Education,skills,programs,experience
# Register your models here.

admin.site.register(Projects)
admin.site.register(Education)
admin.site.register(skills)
admin.site.register(programs)
admin.site.register(experience)