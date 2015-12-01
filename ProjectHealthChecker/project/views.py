import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Project
from .csv_data import CsvData


# Create your views here.


def detail(request, sprint_id):
    return HttpResponse("You're looking at sprint %s." % sprint_id)


def index(request):
    project_list = Project.objects.order_by('-id')
    amount = len(project_list)
    context = {'project_amount': amount,
               'project_list': project_list}


    return render(request, 'project/index.html', context)


def grid(request):
    return render(request, 'project/ui-kits/grid.html')


@ensure_csrf_cookie
def imageTest(request):
    if request.POST.get('click', False):
        data = {}
        c = CsvData
        # c.genreatesom()
        if c.genreatesom():
            data['status'] = 'success'
        else:
            data['status'] = 'fail'
        # randNumber = randint(0, 9)
        # if randNumber % 2 == 0:
        #     data['status'] = 'success'
        # else:
        #     data['status'] = 'fail'
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        return render(request, 'project/imageTest.html')