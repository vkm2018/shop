from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.routers import DefaultRouter

from applications.product.views import CategoryView, ProductView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register('category', CategoryView)
router.register('',ProductView)

urlpatterns = [
    path('', include(router.urls))
    # path('category/', CategoryView.as_view({'get': 'list'}))


]
