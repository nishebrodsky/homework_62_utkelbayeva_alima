from django.views.generic import ListView

from webapp.models.project import Project

class IndexView(ListView):
    template_name = 'index.html'
    model = Project
    context_object_name = 'project'
    ordering = ('title',)
    queryset = Project.objects.all()
