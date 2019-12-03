from django.shortcuts import render
from core.tasks import test,long_task
# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
import json
def index(request):
	test.delay()
	return render(request,"index.html")

def longtask(request):
	task = long_task.apply_async()
	task_id= str(task)
	response1 =json.dumps({'taskid':'/taskstatus/?task_id='+str(task_id)})
	return HttpResponse(response1)

def taskstatus(request):
    taskk =request.GET['task_id']
    print (taskk,"taskk")
    task = long_task.AsyncResult(taskk)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return JsonResponse(response)