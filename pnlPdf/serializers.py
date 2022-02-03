from rest_framework import serializers
from .models import Artigo,  Palavra

class ArtigoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Artigo
        fields = '__all__'



class PalavraSerializer(serializers.ModelSerializer):

    class Meta:

        model = Palavra
        fields = '__all__'
        depth = 1
