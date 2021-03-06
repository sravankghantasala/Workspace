from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from myhome.python_scripts import request_handler as handle

# Create your views here.

@csrf_exempt
def homepage(request):
    if (request.method == 'GET'):
        return render_to_response('index.html')
    elif (request.method == 'POST'):
        return HttpResponse(handle._post(request.POST), 'application/json') #have to use mimetype='application/json' for django 1.6
    