from rest_framework import generics
from rest_framework.views import APIView
from saved_messages.models import Message
from saved_messages.serializers import MessageSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password


class MessageList(APIView):
  def get(self, request):
    message = Message.objects.filter(password__isnull=True)
    serializers = MessageSerializer(message, many=True)
    return Response(serializers.data)

  def post(self, request):
    if 'password' in request.data:
      message = Message.objects.filter(password=make_password(request.data['password'], 'unsalted_sha1'))
      serializers = MessageSerializer(message, many=True)
      return Response(serializers.data)
    else:
      return self.get(request)


class MessageCreate(generics.CreateAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer


class MessageDelete(generics.DestroyAPIView):
  queryset = Message.objects.all()
  serializer_class = MessageSerializer
  
  def perform_destroy(self, instance):
    if instance.password is None:
      instance.delete()
    elif ('password' in self.request.data and 
      check_password(self.request.data['password'], instance.password)):
      instance.delete()
    else:
      raise ValidationError('The password is incorrect')