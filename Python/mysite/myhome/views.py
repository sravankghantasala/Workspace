from django.shortcuts import render_to_response,HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def homepage(request):
    if (request.method == 'GET'):
        return render_to_response('index.html')
    else:
        if (request.POST.__getitem__('topic')  == 'python'):
            data=simplejson.dumps({'data':'python topic'})
            
            return render_to_response('index.html',)