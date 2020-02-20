from django.shortcuts import render

from rest_framework import viewsets
from core.models import *
from .models import *

class MemberViewset(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

