from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AppHospEnCasa.serializers.personaSerializer import *
from AppHospEnCasa.models import Persona
    
class PersonaView(APIView):
    
    def get(self, request, pk = None):
        if pk:
            try:
                item = Persona.objects.get(pk=pk)
                serializer = PersonaSerializer(item)
                answer = {'Persona': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)
            
            except Persona.DoesNotExist:
                answer = {'Mensaje': 'No Hay Persona Registrada Con Id #'+str(pk)+'...'}
                
                return Response(answer, status = status.HTTP_404_NOT_FOUND)
            
        else:
            items = Persona.objects.all()
            listOne = list(items)
            serializer = PersonaSerializer(items, many=True)

            if len(listOne) == 0:
                answer = {'Mensaje': 'No Hay Personas Registradas...'}
                
                return Response(answer, status = status.HTTP_404_NOT_FOUND)
            
            else:
                answer = {'Personas': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)

class UpdatePersonaView(APIView):
     
     def patch(self, request, pk = None):
        persona = Persona.objects.get(pk=pk)
        data = request.data

        persona.telefono = data.get('telefono', persona.telefono)
        
        persona.save()
        serializer = UpdatePersonaSerializer(persona)

        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)