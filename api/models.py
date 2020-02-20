from django.db import models
from rest_framework import serializers

from core.models import *

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = [ 'login', 'name', 'email', 'avatar', 'dob' ]

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [ 'id', 'text', 'member' ]


