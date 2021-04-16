from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from main.models import Category, Invent
from rest_framework import status
from main.serializers import CategorySerializer, CategoryDetailSerializer, InventDetailSerializer, \
    InventCreateSerializer


class PermissionMixin:
    def get_permissions(self):
        if self.action in ['create', 'list']:
            permission = [IsAuthenticated, ]
        elif self.action in ['update', 'partial_update', 'delete']:
            permission = [IsAdminUser, ]
        else:
            permission = []
        return [perm() for perm in permission]



class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]


@api_view(['GET'])
def category_detail(request, slug):
    if request.method == 'GET':
        invent = Invent.objects.filter(category=slug)
        serializer = CategoryDetailSerializer(invent, many=True)
        return Response(serializer.data)


class Pagination(PageNumberPagination):
    page_size = 1

class CategoryDetail(generics.ListAPIView):
    queryset = Invent.objects.all()
    serializer_class = CategoryDetailSerializer
    pagination_class = Pagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = queryset.filter(category=kwargs.get('slug'))
        serializer = CategoryDetailSerializer(queryset, many=True, context={'request': request})
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    def get_serializer_context(self):
        return {'request': self.request}


class InventListView(generics.ListAPIView):
    queryset = Invent.objects.all()
    serializer_class = InventCreateSerializer

    # @action(detail=False, methods=['get'])
    # def search(self, request, pk=None):
    #     q = request.query_params.get('q')
    #     queryset = self.get_queryset()
    #     queryset = queryset.filter(Q(title__icontains=q) | Q(invent_number__icontains=q) | Q(serial_number__icontains=q))
    #     serializer = InventCreateSerializer(queryset, many=True, context={'request': request})
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        q = request.query_params.get('q')
        if q:
            queryset = queryset.filter(
                Q(title__icontains=q) | Q(invent_number__icontains=q) | Q(serial_number__icontains=q))
        serializer = InventCreateSerializer(queryset, many=True, context={'request':request})
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)



class InventDetailView(generics.RetrieveAPIView):
    queryset = Invent.objects.all()
    serializer_class = InventDetailSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class InventCreateView(generics.CreateAPIView):
    queryset = Invent.objects.all()
    serializer_class = InventCreateSerializer
    permission_classes = [IsAuthenticated, ]

    def get_serializer_context(self):
        return {'request' : self.request}



