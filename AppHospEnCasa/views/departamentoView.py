from rest_framework.views import APIView
from AppHospEnCasa.models.paciente import Departamento
from AppHospEnCasa.serializers.departamentoSerializer import DepartamentoSeeSerializer
from rest_framework.response import Response
from rest_framework import status

class DepartamentoSeeView(APIView):

    def get(self, request, pk = None):

        if(pk):
            try:
                element = Departamento.objects.get(pk=pk)
                serializer = DepartamentoSeeSerializer(element)
                answer = {'Departamento': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)
            
            except Departamento.DoesNotExist:
                answer = {'Mensaje': 'El Departamento Con Id #'+str(pk)+', No Existe...'}

                return Response(answer, status = status.HTTP_404_NOT_FOUND)
        
        else:
            elements = Departamento.objects.all()
            dep_list = list(elements)

            if len(dep_list) == 0:
                answer = {'Mensaje': 'No Hay Departamento Registrados...'}

                return Response(answer, status = status.HTTP_404_NOT_FOUND)

            else:
                serializer = DepartamentoSeeSerializer(elements, many=True)
                answer = {'Departamentos': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)