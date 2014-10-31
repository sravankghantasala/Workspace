from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Home.python_scripts import request_handler as handle
from Home.python_scripts._addPost import addPosttoDB as addpost
from django.contrib import messages

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
    
@csrf_exempt 
def addpost(request):
    print(request)
    result = addpost(request.POST)
    print(result)
    if result: messages.error(request,result)
    else: messages.success(request,'Post Added Successfully :)')
    pass


