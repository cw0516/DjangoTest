from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def bori_controller(request):

    if request.method == 'GET':

        response = HttpResponse("hello")
        return response
