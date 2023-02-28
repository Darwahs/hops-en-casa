from rest_framework import serializers
from AppHospEnCasa.serializers.personaSerializer import PersonaSerializer
from AppHospEnCasa.models.profesional_salud import Profesional_salud
from AppHospEnCasa.models.persona import Persona

#----------------------------------------- Ver Información Prof. Salud ---------------------------------------------
class ProfSaludSeeSerializer(serializers.ModelSerializer):
    id_pro = PersonaSerializer()
    id_esp = serializers.StringRelatedField()
    class Meta:
        model = Profesional_salud
        fields = ('id_pro', 'id_esp', 'tarj_pro')
#-------------------------------------------------------------------------------------------------------------------

#----------------------------------------- Crear Información Prof. Salud -------------------------------------------
class ProfSaludSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional_salud
        exclude = ('id_pro',)

class ProfSaludCreateSerializer(serializers.ModelSerializer):
    prof_salud = ProfSaludSerializer()
    class Meta:
        model = Persona
        exclude = ('password',)
    
    def create(self, validated_data):
        prof_saludData = validated_data.pop('prof_salud')
        personaInstance = Persona.objects.create(**validated_data)
        Profesional_salud.objects.create(id_pro = personaInstance, **prof_saludData)

        return personaInstance
    
    def to_representation(self, obj):
        persona = Persona.objects.get(id = obj.id)
        profesional_salud = Profesional_salud.objects.get(pk = obj.id_pro)

        return {
            'id': persona.id,
            'nom_per': persona.nom_per,
            'primerApe_per': persona.primerApe_per,
            'segundoApe_per': persona.segundoApe_per,
            'telefono': persona.telefono,
            'id_doc': persona.id_doc,
            'numdoc_per': persona.numdoc_per,
            'gen_per': persona.gen_per,
            'prof_salud':
            {
                'id_esp': profesional_salud.id_esp,
                'tarj_pro': profesional_salud.tarj_pro
            }
        }
#-------------------------------------------------------------------------------------------------------------------

