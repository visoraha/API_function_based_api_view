from django.shortcuts import render
from app.serializers import *
from rest_framework.decorators import api_view
from app.models import *
from rest_framework.response import Response

# Create your views here.

@api_view()
def Employdata(request):
    EQS=Employ.objects.all()
    ESD=EmployModel_Serilizer(EQS,many=True)
    return Response(ESD.data)
