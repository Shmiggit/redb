from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello World!!')

def addProject(request):
    return render(request, 'addProject.html')