from rest_framework.serializers import ModelSerializer
from AppHospEnCasa.models.paciente import Ciudad
from AppHospEnCasa.serializers.departamentoSerializer import DepartamentoSeeSerializer

#--------------------------------------- Infromación Ciudad Con Id Dep. --------------------------------------------
class CiudadOriginalSerializer(ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id_ciudad', 'id_dep',  'nom_ciudad')
#-------------------------------------------------------------------------------------------------------------------

#------------------------------------------- Ver Información Ciudad ------------------------------------------------
class CiudadSeeSerializer(ModelSerializer):
    id_dep = DepartamentoSeeSerializer()
    class Meta:
        model = Ciudad
        fields = ('id_ciudad', 'id_dep',  'nom_ciudad')
#-------------------------------------------------------------------------------------------------------------------