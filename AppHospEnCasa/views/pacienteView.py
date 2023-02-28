from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from proyectoHospEnCasa import settings
from AppHospEnCasa.serializers.pacienteSerializer import (
    PacientePersonaSeralizer, PacienteSeeSerializer,
    UpdatePacienteSerializer
)
from AppHospEnCasa.models.paciente import Ciudad, Paciente

class PacienteSeeView(APIView):

    def get(self, request, pk = None):
        if pk:
            try:
                item = Paciente.objects.get(pk=pk)
                serializer = PacienteSeeSerializer(item)
                answer = {'Paciente': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)
            
            except Paciente.DoesNotExist:
                answer = {'Mensaje': 'No Hay Paciente Registrado Con Id #'+str(pk)+'...'}

                return Response(answer, status = status.HTTP_404_NOT_FOUND)
        
        else:
            items = Paciente.objects.all()
            mainList = list(items)
            serializer = PacienteSeeSerializer(items, many=True)

            if len(mainList) == 0:
                answer = {'Mensaje': 'No Hay Pacientes Registrados...'}

                return Response(answer, status = status.HTTP_404_NOT_FOUND)
            
            else:
                answer = {'Pacientes': serializer.data}

                return Response(answer, status = status.HTTP_200_OK)

class CrearPacienteView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = PacientePersonaSeralizer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()

        tokenData = {
            "numdoc_per": request.data['numdoc_per'],
            "password": request.data['numdoc_per']
        }
        tokenSerializer = TokenObtainPairSerializer(data = tokenData)
        tokenSerializer.is_valid(raise_exception = True)

        return Response(tokenSerializer.validated_data, status = status.HTTP_201_CREATED)

class UpdatePacienteView(APIView):

    def patch(self, request, pk = None):
        paciente = Paciente.objects.get(pk=pk)
        data = request.data

        idCiudad = Ciudad.objects.only('id_ciudad').get(id_ciudad = data['id_ciudad'])

        paciente.dir_pac = data.get("dir_pac", paciente.dir_pac)
        paciente.id_ciudad = idCiudad
        paciente.lon_pac = data.get("lon_pac", paciente.lon_pac)
        paciente.lat_pac = data.get("lat_pac", paciente.lat_pac)
        
        paciente.save()
        serializer = UpdatePacienteSerializer(paciente)

        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

class PacienteAccessInfoView(generics.RetrieveAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSeeSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if(valid_data['user_id'] != kwargs['pk']): # 'user_id' es un elemento que ya se encuentra por defecto
            answer = {'Mensaje':'No está autorizado'} # En la variable 'valid_data'
            return Response(answer, status = status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)