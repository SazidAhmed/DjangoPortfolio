from django.contrib import admin
from .models import Project
from .models import Experience
from .models import About
from .models import Interest
from .models import Skill

# Register your models here.

admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(About)
admin.site.register(Interest)
admin.site.register(Skill)

