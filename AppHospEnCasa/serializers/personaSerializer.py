from AppHospEnCasa.models.persona import Persona
from rest_framework import serializers

#-------------------------------------------- Ver Información Persona ----------------------------------------------
class PersonaSerializer(serializers.ModelSerializer):
    id_doc = serializers.StringRelatedField()
    class Meta:
        model = Persona
        fields = ('id', 'nom_per', 'primerApe_per', 'segundoApe_per', 'telefono', 'id_doc', 'numdoc_per', 'gen_per')
#-------------------------------------------------------------------------------------------------------------------

#--------------------------------------- Actualizar Información Persona --------------------------------------------
class UpdatePersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('telefono',)
#-------------------------------------------------------------------------------------------------------------------