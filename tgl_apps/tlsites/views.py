
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse

# libraries imports
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# app imports
#from models import MyriadDetermination
#from serializers import MyriadDeterminationSerializer_OneObject, MyriadDeterminationNSerializer, MyriadHailDeterminationSerializer


#import xml.etree.ElementTree as ET
#from xml.dom.minidom import Text, Element

#import cPickle as pickle
#import urllib


#class MyriadDeterminationViewSet(viewsets.ModelViewSet):
#    queryset = MyriadDetermination.objects.all()
#    serializer_class = MyriadDeterminationSerializer_OneObject


def index(request):
    return HttpResponse('hello')