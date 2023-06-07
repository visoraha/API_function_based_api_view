from rest_framework import serializers
from app.models import *

class EmployModel_Serilizer(serializers.ModelSerializer):
    class Meta:
        model=Employ
        fields='__all__'