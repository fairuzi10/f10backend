from rest_framework import serializers
from saved_messages.models import Message
from django.contrib.auth.hashers import make_password


class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ('pk', 'text', 'password', )
    extra_kwargs = {'password': {'write_only': True}}