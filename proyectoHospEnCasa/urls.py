"""pacientesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from AppHospEnCasa.views.departamentoView import *
from AppHospEnCasa.views.ciudadView import *
from AppHospEnCasa.views.personaView import *
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from AppHospEnCasa.views.profSaludView import *
from AppHospEnCasa.views.pacienteView import *
from AppHospEnCasa.views.familiarPacienteView import *

app_name = 'pacientesApp'
urlpatterns = [
    path('Admin/', admin.site.urls),

    #--------------------------- Departamento -------------------------------
    path('Departamento/', DepartamentoSeeView.as_view()),
    path('Departamento/<int:pk>', DepartamentoSeeView.as_view()),
    #------------------------------------------------------------------------

    #------------------------------ Ciudad ----------------------------------
    path('Ciudad/', CiudadView.as_view()),
    path('Ciudad/<int:pk>', CiudadView.as_view()),
    #------------------------------------------------------------------------

    #------------------------------ Persona ---------------------------------
    path('Persona/', PersonaView.as_view()),
    path('Persona/<int:pk>', PersonaView.as_view()),
    path('Actualizar_persona/<int:pk>', UpdatePersonaView.as_view()),
    #------------------------------------------------------------------------

    #--------------------------- Iniciar Sesión -----------------------------
    path('Login/', TokenObtainPairView.as_view()),
    path('Refresh/', TokenRefreshView.as_view()),
    #------------------------------------------------------------------------

    #----------------------------- Prof_salud -------------------------------
    path('Crear_prof_salud/', CrearProfSaludView.as_view()),
    path('Profesional_salud/', ProfSaludView.as_view()),
    path('Profesional_salud/<int:pk>', ProfSaludView.as_view()),
    #------------------------------------------------------------------------

    #--------------------------- Familiar Paciente --------------------------
    path('Crear_familiar_paciente/', CrearFamiliarPacienteView.as_view()),
    path('Familiar_paciente/', FamiliarPacienteView.as_view()),
    path('Familiar_paciente/<int:pk>', FamiliarPacienteView.as_view()),
    path('Actualizar_familiar_paciente/<int:pk>', UpdateFamiliarPaciente.as_view()),
    #------------------------------------------------------------------------

    #------------------------------ Paciente --------------------------------
    path('Crear_paciente/', CrearPacienteView.as_view()),
    path('Paciente/', PacienteSeeView.as_view()),
    path('Paciente/<int:pk>', PacienteSeeView.as_view()),
    path('Paciente_Autenticado_Info/<int:pk>', PacienteAccessInfoView.as_view()),
    path('Actualizar_paciente/<int:pk>', UpdatePacienteView.as_view()),
    #------------------------------------------------------------------------
   ]
