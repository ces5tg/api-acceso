from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .models import *
from .serializer import *
from django.http import Http404, JsonResponse
import subprocess
from rest_framework.decorators import api_view
class IndexView(APIView):
    
    def get(self,request):
        context = {'mensaje':'servidor activo API FINAL'}
        return Response(context)


class ZonaViewSet(viewsets.ModelViewSet):
    queryset = Zona.objects.all()
    serializer_class = ZonaSerializer

class TipoAulaViewSet(viewsets.ModelViewSet):
    queryset = TipoAula.objects.all()
    serializer_class = TipoAulaSerializer


class AulaViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

class DispositivoViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo.objects.all()
    serializer_class = DispositivoSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class DetalleAccesoViewSet(viewsets.ModelViewSet):
    queryset = DetalleAcceso.objects.all()
    serializer_class = DetalleAccesoSerializer


class AccesoViewSet(viewsets.ModelViewSet):
    queryset = Acceso.objects.all()
    serializer_class = AccesoSerializer

class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class HorarioPersonaViewSet(viewsets.ModelViewSet):
    queryset = HorarioPersona.objects.all()
    serializer_class = HorarioPersonaSerializer


class HorarioViewSet(APIView):
    def get(self, request):
        aula = request.GET.get('aula_id')#aula
        queryset = Horario.objects.all()
        if aula:
            queryset = queryset.filter(aula = aula).order_by('hora_inicio')
        serializer = HorarioSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return Horario.objects.get(pk=pk)
        except Horario.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = HorarioSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=204)

class HorarioProfesorViewSet(APIView):
    def get(self, request):
        horario = request.GET.get('horario_id')
        queryset = HorarioPersona.objects.all()
        if horario:
            queryset = queryset.filter(horario = horario)
        serializer = HorarioPersonaSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HorarioPersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get_object(self, pk):
        try:
            return HorarioPersona.objects.get(pk=pk)
        except HorarioPersona.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = HorarioPersonaSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response(status=204)
    
class HorarioPersonaView(APIView):
    
    def get(self,request):
        aula = request.GET.get('horario_id')
        queryset = HorarioPersona.objects.all()
        if aula:
            queryset = queryset.filter(aula = aula).order_by('hora_inicio')

        serHorarioPersona = HorarioPersonaSerializer(queryset,many=True)
        return Response(serHorarioPersona.data)
    
    def post(self,request):
        serHorarioPersona = HorarioPersonaSerializer(data=request.data)
        serHorarioPersona.is_valid(raise_exception=True)
        serHorarioPersona.save()
        
        return Response(serHorarioPersona.data)
    
class HorarioPersonaDetailView(APIView):
    
    def get(self,request,horario_id):
        dataHorarioPersona = HorarioPersona.objects.get(pk=horario_id)
        serHorarioPersona = HorarioPersonaSerializer(dataHorarioPersona)
        return Response(serHorarioPersona.data)
    
    def put(self,request,horario_id):
        dataHorarioPersona = HorarioPersona.objects.get(pk=horario_id)
        serHorarioPersona = HorarioPersonaSerializer(dataHorarioPersona,data=request.data)
        serHorarioPersona.is_valid(raise_exception=True)
        serHorarioPersona.save()
        return Response(serHorarioPersona.data)
    
    def delete(self,request,horario_id):
        dataHorarioPersona = HorarioPersona.objects.get(pk=horario_id)
        serHorarioPersona = HorarioPersonaSerializer(dataHorarioPersona)
        dataHorarioPersona.delete()
        return Response(serHorarioPersona.data)







class HorarioView(APIView):
    
    def get(self,request):
        aula = request.GET.get('aula_id')
        queryset = Horario.objects.all()
        if aula:
            queryset = queryset.filter(aula = aula).order_by('hora_inicio')

        serHorario = HorarioSerializer(queryset,many=True)
        return Response(serHorario.data)
    
    def post(self,request):
        serHorario = HorarioSerializer(data=request.data)
        serHorario.is_valid(raise_exception=True)
        serHorario.save()
        
        return Response(serHorario.data)
    
class HorarioDetailView(APIView):
    
    def get(self,request,horario_id):
        dataHorario = Horario.objects.get(pk=horario_id)
        serHorario = HorarioSerializer(dataHorario)
        return Response(serHorario.data)
    
    def put(self,request,horario_id):
        dataHorario = Horario.objects.get(pk=horario_id)
        serHorario = HorarioSerializer(dataHorario,data=request.data)
        serHorario.is_valid(raise_exception=True)
        serHorario.save()
        return Response(serHorario.data)
    
    def delete(self,request,horario_id):
        dataHorario = Horario.objects.get(pk=horario_id)
        serHorario = HorarioSerializer(dataHorario)
        dataHorario.delete()
        return Response(serHorario.data) 