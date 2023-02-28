from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from AppHospEnCasa.models.profesional_salud import Profesional_salud
from AppHospEnCasa.serializers.profSaludSerializer import (
ProfSaludCreateSerializer, ProfSaludSeeSerializer
)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CrearProfSaludView(views.APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = ProfSaludCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "numdoc_per": request.data['numdoc_per'],
            "password": request.data['numdoc_per']
        }
        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception = True)

        return Response(tokenSerializer.validated_data, status = status.HTTP_201_CREATED)

class ProfSaludView(views.APIView):

    def get(self, request, pk = None):

        if pk:
            try:
                item = Profesional_salud.objects.get(pk=pk)
                serializer = ProfSaludSeeSerializer(item)
                answer = {'Profesional_salud': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)
            
            except Profesional_salud.DoesNotExist:
                answer = {'Mensaje': 'No Hay Profesional_salud Registrado Con Id #'+str(pk)+'...'}

                return Response(answer, status = status.HTTP_404_NOT_FOUND)
        
        else:
            items = Profesional_salud.objects.all()
            mainList = list(items)
            serializer = ProfSaludSeeSerializer(items, many=True)

            if len(mainList) == 0:
                answer = {'Mensaje': 'No Hay Profesionales_salud Registrados...'}

                return Response(answer, status = status.HTTP_404_NOT_FOUND)

            else:
                answer = {'Profesionales_salud': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)