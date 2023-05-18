from django.shortcuts import render

from .models import Place, Place1


# from django.http import HttpResponse
# Create your views here.

def demo(request):
    obj = Place.objects.all()
    ob = Place1.objects.all()
    return render(request, "index.html", {'result': obj, 'results': ob})
