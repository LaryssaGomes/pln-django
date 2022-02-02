from rest_framework import serializers
from .models import Artigo, Sentenca, Palavra

class ArtigoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Artigo
        fields = '__all__'


class SentencaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sentenca
        fields = '__all__'

class PalavraSerializer(serializers.ModelSerializer):

    class Meta:

        model = Palavra
        fields = '__all__'
