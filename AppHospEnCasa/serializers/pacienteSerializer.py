from rest_framework import serializers
from AppHospEnCasa.models.paciente import Paciente
from AppHospEnCasa.models.persona import Persona
from AppHospEnCasa.serializers.personaSerializer import PersonaSerializer
from AppHospEnCasa.serializers.familiarSerializer import FamiliarSeeSerializer
from AppHospEnCasa.serializers.ciudadSerializer import CiudadSeeSerializer

#------------------------------------------ Ver Información Paciente -----------------------------------------------
class PacienteSeeSerializer(serializers.ModelSerializer):
    id_pac = PersonaSerializer()
    id_fam = FamiliarSeeSerializer()
    id_pro = serializers.StringRelatedField()
    id_ciudad = CiudadSeeSerializer()
    class Meta:
        model = Paciente
        fields = ('id_pac', 'fech_nac', 'rh_pac', 'id_fam', 'id_pro', 'dir_pac', 'id_ciudad', 'lon_pac', 'lat_pac')
#-------------------------------------------------------------------------------------------------------------------

#---------------------------------------- Crear Información Paciente -----------------------------------------------
class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        exclude = ('id_pac',)

class PacientePersonaSeralizer(serializers.ModelSerializer):
    paciente = PacienteSerializer()
    class Meta:
        model = Persona
        exclude = ('password',)
    
    def create(self, validated_data):
        pacienteData = validated_data.pop('paciente')
        personaInstance = Persona.objects.create(**validated_data)
        Paciente.objects.create(id_pac = personaInstance, **pacienteData)

        return personaInstance
    
    def to_representation(self, obj):
        persona = Persona.objects.get(id = obj.id)
        pacient = Paciente.objects.get(id_pac = obj.id_pac)

        return {
            'id': persona.id,
            'nom_per': persona.nom_per,
            'primerApe_per': persona.primerApe_per,
            'segundoApe_per': persona.segundoApe_per,
            'telefono': persona.telefono,
            'id_doc': persona.id_doc,
            'numdoc_per': persona.numdoc_per,
            'gen_per': persona.gen_per,
            'paciente':
            {
                'fech_nac': pacient.fech_nac,
                'rh_pac': pacient.rh_pac,
                'id_fam': pacient.id_fam,
                'id_pro': pacient.id_pro,
                'dir_pac': pacient.dir_pac,
                'id_ciudad': pacient.id_ciudad,
                'lon_pac': pacient.lon_pac,
                'lat_pac': pacient.lat_pac
            }
        }
#-------------------------------------------------------------------------------------------------------------------

#---------------------------------------- Actualizar Información Paciente-------------------------------------------
class UpdatePacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
#-------------------------------------------------------------------------------------------------------------------