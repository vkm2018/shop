from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet, ModelViewSet

from applications.product.models import Category
from applications.product.seriallizers import CategorySerializers
from rest_framework.response import Response

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

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



