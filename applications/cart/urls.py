from django.urls import path
from rest_framework.routers import DefaultRouter

from applications.cart.views import OrderView

router = DefaultRouter()
router.register('', OrderView)

# urlpatterns += router.urls
urlpatterns = []
urlpatterns.extend(router.urls)
