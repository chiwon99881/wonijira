from django.shortcuts import render
from . import models


def all_projects(request):

    projects = models.Project.objects.all()

    return render(request, "projects/all_projects.html", context={"projects": projects})
