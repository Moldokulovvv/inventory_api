from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.response import Response
from acts.models import Akt
from acts.serializers import ActSerializer
from django.db.models import Q

from main.views import PermissionMixin

class ActViewSet(PermissionMixin,viewsets.ModelViewSet):
    queryset = Akt.objects.all()
    serializer_class = ActSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(Q(sender=request.user) | Q(recipient=request.user))
        serializers = ActSerializer(queryset, many=True, context={'request' : request})
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializers.data, status=status.HTTP_200_OK)

    def get_serializer_context(self):
        return {'request': self.request}




