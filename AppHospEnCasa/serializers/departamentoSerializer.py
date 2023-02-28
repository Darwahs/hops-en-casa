from rest_framework import serializers
from AppHospEnCasa.models.paciente import Departamento

class DepartamentoSeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id_dep', 'nom_dep')