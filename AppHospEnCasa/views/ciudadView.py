from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from AppHospEnCasa.models.paciente import Ciudad
from AppHospEnCasa.serializers.ciudadSerializer import CiudadOriginalSerializer

class CiudadView(APIView):

    def get(self, request, pk = None):
        
        if pk:
            try:
                city = Ciudad.objects.get(pk=pk)
                serializer = CiudadOriginalSerializer(city)
                answer = {'Ciudad': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)
            
            except Ciudad.DoesNotExist:
                answer = {'Mensaje': 'La Ciudad Con Id #'+str(pk)+', No Existe...'}

                return Response(answer, status = status.HTTP_404_NOT_FOUND)
        
        else:
            cities = Ciudad.objects.all()
            cities_list = list(cities)

            if len(cities_list) == 0:
                answer = {'Mensaje': 'No Hay Ciudades Registradas...'}

                return Response(answer, status = status.HTTP_404_NOT_FOUND)

            else:
                serializer = CiudadOriginalSerializer(cities, many=True)
                answer = {'Ciudades': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)