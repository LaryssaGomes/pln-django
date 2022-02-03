from django.urls import include, path
from rest_framework import serializers
from . import views

from .models import Artigo, Palavra
from rest_framework import viewsets, routers


class PalavraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palavra
        fields = '__all__'

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Palavra.objects.select_related()
    serializer_class = PalavraSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'artigo', UserViewSet)


urlpatterns = [
   path('artigo/', include(router.urls)),
   path('artigo/salvando', views.member_api),
   path('artigo/list', views.lista_artigos_palavras),
]