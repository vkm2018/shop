from django.urls import path, include
from rest_framework.routers import DefaultRouter

from applications.product.views import CategoryView

router = DefaultRouter()
router.register('category', CategoryView)

urlpatterns = [
    path('', include(router.urls))
    # path('category/', CategoryView.as_view({'get': 'list'}))


]