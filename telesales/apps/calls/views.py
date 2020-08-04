from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    ListAPIView,
    DestroyAPIView,
)
from rest_framework.response import Response
from rest_framework import status
from .serializers import (CallSerializer, UpdateDispositionSerializer,)
from .renderers import CallRenderer, CallsRenderer
from .models import Call
from ..utils.emailer import send_email
from ..utils.messenger import sendsms

# Create your views here.


class CreateCallView(CreateAPIView):
    serializer_class = CallSerializer
    renderer_classes = (CallRenderer,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        request_data = request.data.get('call', {})
        if request_data['escalation']:
            email_data = {'sender': 'telesales@gmail.com',
                          'recipient': request_data['caller_email'],
                          'subject': 'Escalation Alert'}
            send_email(request=request, data=email_data,)
            # sendsms(request_data['caller_phone'], 'Hello test escalation')
        serializer = self.serializer_class(data=request_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateDispositionView(UpdateAPIView):
    serializer_class = UpdateDispositionSerializer
    renderer_classes = (CallRenderer,)
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        qid = self.kwargs.get(self.lookup_url_kwarg)
        return Call.objects.filter(id=qid)

    def put(self, request, *args, **kwargs):
        request_data = request.data.get('call', {})
        queryset = self.get_queryset()

        if not queryset:
            return Response({'error': 'Call was not found'}, status=status.HTTP_400_BAD_REQUEST)

        updated_call = self.serializer_class().update(
            queryset[0], request_data)
        return Response(data=self.serializer_class(updated_call).data, status=status.HTTP_201_CREATED)


class GetAllCallsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CallsRenderer,)
    serializer_class = CallSerializer

    def get_queryset(self):
        return Call.objects.all().filter().order_by('id')


class GetAllUserCallsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (CallsRenderer,)
    serializer_class = CallSerializer
    lookup_url_kwarg = 'name'

    def get_queryset(self):
        name = self.kwargs.get(self.lookup_url_kwarg)
        return Call.objects.all().filter(caller_name=name).order_by('id')


class DeleteCallView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        cid = self.kwargs.get(self.lookup_url_kwarg)
        return Call.objects.filter(id=cid)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if not queryset:
            return Response({'error': 'No such call was found.'}, status=status.HTTP_404_NOT_FOUND)

        queryset.delete()
        return Response({'response': 'Call was deleted.'}, status=status.HTTP_200_OK)
