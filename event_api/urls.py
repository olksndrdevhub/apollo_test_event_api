from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import index, EventViewSet, EventTypeViewSet


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'event-types', EventTypeViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', index, name="index_view"),
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', obtain_auth_token, name='api_token_auth'),

]
