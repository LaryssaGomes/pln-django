from django.urls import include, path
from rest_framework import serializers
from . import views
from .models import Artigo
from rest_framework import viewsets, routers


class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = '__all__'

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Artigo.objects.all()
    serializer_class = ArtigoSerializer


    

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'artigo', UserViewSet)


urlpatterns = [
   path('artigo/', include(router.urls)),
   path('artigo/m embers2', views.member_api),
]