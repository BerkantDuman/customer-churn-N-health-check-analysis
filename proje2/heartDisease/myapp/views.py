from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .serializers import PersonSerializer, ValuesSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
from .models import Person, Values


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.get_queryset()

    # Get All
    def list_all(self, request, *args, **kwargs):
        qs = Person.objects.all()

        serializer = PersonSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_id(self, request, *args, **kwargs):
        qs = Person.objects.all()

        id = str(kwargs['id'])
        if id is not None:
            qs = qs.filter(id=id)

        serializer = PersonSerializer(qs, many=True)

        if qs.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def login(self, request, *args, **kwargs):
        qs = Person.objects.filter(username=request.data["username"],
                                   password=request.data["password"])
        if qs.exists():
            serializer = PersonSerializer(qs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Invalid cridentials", status=status.HTTP_401_UNAUTHORIZED)


class ValueView(viewsets.ModelViewSet):
    queryset = Person.objects.get_queryset()

    def list_all(self, request, *args, **kwargs):
        qs = Values.objects.all()

        serializer = ValuesSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_by_id(self, request, *args, **kwargs):
        qs = Values.objects.all()

        id = str(kwargs['id'])
        if id is not None:
            qs = qs.filter(id=id)

        serializer = ValuesSerializer(qs, many=True)

        if qs.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get_by_person(self, request, *args, **kwargs):
        qs = Values.objects.all()

        person_id = str(kwargs['person_id'])
        if person_id is not None:
            qs = qs.filter(person=person_id)

        serializer = ValuesSerializer(qs, many=True)

        if qs.exists():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
