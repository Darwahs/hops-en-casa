from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from AppHospEnCasa.models.familiar_paciente import FamiliarPaciente
from AppHospEnCasa.serializers.familiarSerializer import *

class FamiliarPacienteView(APIView):

    def get(self, request, pk = None):
        if pk:
            try:
                element = FamiliarPaciente.objects.get(pk=pk)
                serializer = FamiliarSeeSerializer(element)
                answer = {'Familiar_paciente': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)
            
            except FamiliarPaciente.DoesNotExist:
                answer = {'Mensaje': 'No Hay Familiar Registrado Con Id #'+str(pk)+'...'}
                
                return Response(answer, status = status.HTTP_404_NOT_FOUND)
        
        else:
            elements = FamiliarPaciente.objects.all()
            mainList = list(elements)
            serializer = FamiliarSeeSerializer(elements, many=True)

            if len(mainList) == 0:
                answer = {'Mensaje': 'No Hay Familiar De Pacientes Registrados...'}
                
                return Response(answer, status = status.HTTP_404_NOT_FOUND)
            
            else:
                answer = {'Familiar_pacientes': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)

class CrearFamiliarPacienteView(APIView):

    def post(self, request):
        serializer = FamiliarPersonaSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        tokenData = {
            "numdoc_per": request.data['numdoc_per'],
            "password": request.data['numdoc_per']
        }
        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception = True)

        return Response(tokenSerializer.validated_data, status = status.HTTP_201_CREATED)

class UpdateFamiliarPaciente(APIView):

    def patch(self, request, pk = None):
        familiar = FamiliarPaciente.objects.get(pk=pk)
        data = request.data

        familiar.email_fam = data.get('email_fam', familiar.email_fam)
        
        familiar.save()
        serializer = UpdateFamiliarPacienteSerializer(familiar)

        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)