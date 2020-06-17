from django.shortcuts import render, get_object_or_404
from .models import Project
from .models import Experience
from .models import About
from .models import Interest
from .models import Skill

# Create your views here.
def index(request):
    projects = Project.objects.all()
    experience = Experience.objects.all()
    about = About.objects.all()
    interest = Interest.objects.all()
    skill = Skill.objects.all()
    context = {
        'projects': projects,
        'experience': experience,
        'about': about,
        'interest': interest,
        'skill': skill,
    }
    return render(request, 'project/index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project':project
    }
    return render(request, 'project/detail.html', context)
