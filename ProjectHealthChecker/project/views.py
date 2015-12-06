import json

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Project, TrainingData
from project.somtrain import somtrain
from project.predict_class import predictor
from random import randint


# Create your views here.


def detail(request, sprint_id):
    return HttpResponse("You're looking at sprint %s." % sprint_id)


def index(request):
    project_list = Project.objects.order_by('id')
    amount = len(project_list)
    context = {'project_amount': amount,
               'project_list': project_list}


    return render(request, 'project/index.html', context)


def grid(request):
    return render(request, 'project/ui-kits/grid.html')


# def evaluate(request):
#     if request.POST.get('click', False):
#         data = []
#         p = predictor()
#         result = p.makePrediction()
#         if result == 'success':
#             data['status'] = 'success'
#         else:
#             data['status'] = 'fail'
#         # randNumber = randint(0, 9)
#         # if randNumber % 2 == 0:
#         #     data['status'] = 'success'
#         # else:
#         #     data['status'] = 'fail'
#         return HttpResponse(json.dumps(data), content_type="application/json")
#     else:
#         return render(request, 'project/imageTest.html')


def form(request):
    if request.POST.get('click', False):
        project_completion = request.POST.get('pr_cmp')
        spi= request.POST.get('spi')
        cpi= request.POST.get('cpi')
        developer_experience= request.POST.get('dev_exp')
        test_cases_passed= request.POST.get('test_cases')
        task_completion= request.POST.get('task_cmplt')

        data = {}
        p = predictor()
        result = p.makePrediction(project_completion,spi,cpi,developer_experience,test_cases_passed,task_completion)
        if result == 'success':
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
        lastRecord = TrainingData.objects.all().order_by('-id')[0]
        context = {'project_completion': lastRecord.completed_project_duration,
                   'spi': lastRecord.spi,
                   'cpi': lastRecord.cpi,
                   'developer_experience': lastRecord.developer_experience,
                   'task_completion': lastRecord.task_completion,
                   'test_cases_passed': lastRecord.test_cases_passed,
                   'sprint_condition': lastRecord.sprint_condition}
        return render(request, 'project/ui-kits/form.html', context)


@ensure_csrf_cookie
def imageTest(request):
    #if request.POST.get('click', False):
    data = {}
    c = somtrain
    # c.genreatesom()
    print 'before if'
    if c.genreatesom():
        data['status'] = 'success'
    else:
        data['status'] = 'fail'
    # randNumber = randint(0, 9)
    # if randNumber % 2 == 0:
    #     data['status'] = 'success'
    # else:
    #     data['status'] = 'fail'
    #return HttpResponse(json.dumps(data), content_type="application/json")
    #else:
    return render(request, 'project/imageTest.html')