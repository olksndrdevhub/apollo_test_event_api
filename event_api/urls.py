from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import index, EventViewSet


router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', index, name="index_view"),
    path('api/v1/', include(router.urls)),

]
