from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Milestone
from .models import Project

# Create your views here.
def detail(request, milestone_id):
    return HttpResponse("You're looking at milestone %s." % milestone_id)

def index(request):
    project_list = Project.objects.order_by('-id')
    amount = len(project_list)
    context = {'project_amount': amount,
               'project_list': project_list}
    return render(request, 'project/index.html', context)

def grid(request):
    return render(request, 'project/ui-kits/grid.html')