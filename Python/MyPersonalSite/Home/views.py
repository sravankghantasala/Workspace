from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Home.python_scripts import request_handler as handle

# Create your views here.

@csrf_exempt
def homepage(request):
    print(request.method)
    if (request.method == 'GET'):
        return render_to_response('index.html', handle._get())
    elif (request.method == 'POST'):
        d = handle._post(request.POST)
        print(d)
        return HttpResponse(d, 'application/json') #have to use mimetype='application/json' for django  <1.6
    