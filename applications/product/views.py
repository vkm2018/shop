from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ViewSet, ModelViewSet

from applications.product.models import Category, Product
from applications.product.permissions import CustomIsAdmin
from applications.product.seriallizers import CategorySerializers, ProductSerializer
from rest_framework.response import Response


class LargeResultSetPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page_size'
    max_page_size = 10000


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = LargeResultSetPagination
    # permission_classes = [IsAdminUser]
    permission_classes = [CustomIsAdmin]


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category', 'owner']
    ordering_fields = ['name', 'id']
    search_fields = ['name', 'descriptions']


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     filter_category = self.request.query_params.get('category')
    #     if filter_category:
    #         queryset = queryset.filter(category=filter_category)
    #     return queryset




# class CategoryView(ViewSet):
#
#     def list(self, request):
#         queryset = Category.objects.all()
#         serializer = CategorySerializers(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = CategorySerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status =201)
#         return Response(serializer.errors, status=400)



