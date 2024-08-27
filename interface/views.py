from django.shortcuts import render
from .models import Materials, Bmaterials
from .serializers import serialize_interface, serialize_data, serialize_nested_data
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')

def material_list(request):
    materials = Materials.objects.all()
    return JsonResponse(serialize_interface(materials), safe=False)


def bmaterials_list(request):
    chartmaterials = Bmaterials.objects.all()[:10] 
    return JsonResponse(serialize_data(chartmaterials), safe=False)


def nested_list(request):
    nested_materials = Bmaterials.objects.all()
    return JsonResponse(serialize_nested_data(nested_materials), safe=False)