
from rest_framework import serializers
from ..models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Empleado
        depth   = 1
        fields  = '__all__'