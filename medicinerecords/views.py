from django.shortcuts import render
from .models import medicines
from .serializers import MedicineSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

@csrf_exempt
def medicine_list(request):
    """
    List all code records, or create a new snippet.
    """
    if request.method == 'GET':
        records = medicines.objects.filter(name__startswith = request.GET['name'])
        serializer = MedicineSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False)