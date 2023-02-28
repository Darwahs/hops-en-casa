from rest_framework import serializers
from AppHospEnCasa.models.familiar_paciente import FamiliarPaciente
from AppHospEnCasa.models.persona import Persona
from AppHospEnCasa.models.paciente import Paciente
from .personaSerializer import *

#------------------------------------- Ver Información Familiar Paciente -------------------------------------------
class SeeInfoPaciente(serializers.ModelSerializer):
    id_pac = PersonaSerializer()
    id_pro = serializers.StringRelatedField()
    id_ciudad = serializers.StringRelatedField()
    class Meta:
        model = Paciente
        fields = ('id_pac', 'fech_nac', 'rh_pac', 'id_pro', 'dir_pac', 'id_ciudad', 'lon_pac', 'lat_pac')

class FamiliarSeeSerializer(serializers.ModelSerializer):
    id_fam = PersonaSerializer()
    class Meta:
        model = FamiliarPaciente
        fields = ('id_fam', 'paren_fam', 'email_fam')
#-------------------------------------------------------------------------------------------------------------------

#-------------------------------------- Crear Información Familiar Paciente ----------------------------------------
class FamiliarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamiliarPaciente
        exclude = ('id_fam',)

class FamiliarPersonaSerializer(serializers.ModelSerializer):
    fami_pac = FamiliarSerializer()
    class Meta:
        model = Persona
        exclude = ('password',)
    
    def create(self, validated_data):
        familiarData = validated_data.pop('fami_pac')
        personaInstance = Persona.objects.create(**validated_data)
        FamiliarPaciente.objects.create(id_fam = personaInstance, **familiarData)

        return personaInstance
    
    def to_representation(self, obj):
        persona = Persona.objects.get(id = obj.id)
        familiar = FamiliarPaciente.objects.get(id_fam = obj.id_fam)

        return {
            'id': persona.id,
            'nom_per': persona.nom_per,
            'primerApe_per': persona.primerApe_per,
            'segundoApe_per': persona.segundoApe_per,
            'telefono': persona.telefono,
            'id_doc': persona.id_doc,
            'numdoc_per': persona.numdoc_per,
            'gen_per': persona.gen_per,
            'fami_pac':
            {
                'paren_fam': familiar.paren_fam,
                'email_fam': familiar.email_fam
            }
        }
#-------------------------------------------------------------------------------------------------------------------

#--------------------------------------------- Actualizar Información ----------------------------------------------
class UpdateFamiliarPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamiliarPaciente
        fields = '__all__'
#-------------------------------------------------------------------------------------------------------------------