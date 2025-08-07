from django.shortcuts import render
from .models import Profile, Skill, Project


# Create your views here.
def index(request):
    profile = Profile.objects.first()  # Assuming you want to display the first profile
    skills = Skill.objects.all() if profile else Skill.objects.none()
    projects = Project.objects.all() if profile else Project.objects.none()
    context = {
        "title": "Home",
        "message": "Welcome to the Home Page!",
        "profile": profile,
        "skills": skills,
        "projects": projects,
    }
    return render(request, "homeapp/index.html", context, content_type="text/html")
