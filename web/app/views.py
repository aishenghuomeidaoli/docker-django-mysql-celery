# -*- coding: utf-8 -*-
from django.core import serializers
from django.http.response import JsonResponse
from django.shortcuts import render

from .models import MathTask
from .tasks import math


def index(request):
    if request.method != 'POST':
        return render(request, 'app/index.html')
    form = request.POST
    task_type = form.get('task_type')
    x = form.get('x')
    y = form.get('y')
    if task_type and x and y:
        row = MathTask(task_type=task_type, x=x, y=y)
        row.save()
        math.delay(row.id)
        return render(request,
                      'app/index.html',
                      context={'msg': 'success, task id: %s' % row.id})
    else:
        return render(request,
                      'app/index.html',
                      context={'msg': 'failed, parameters error'})


def query(request):
    rows = MathTask.objects.filter(is_valid=True)
    data = serializers.serialize("python", rows)
    return JsonResponse({
        'data': data
    })
