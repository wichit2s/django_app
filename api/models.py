from django.db import models
from rest_framework import serializers

from core.models import *

class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = [ 'username', 'first_name', 'last_name', 'email', 'avatar', 'dob' ]

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [ 'id', 'text', 'member' ]


