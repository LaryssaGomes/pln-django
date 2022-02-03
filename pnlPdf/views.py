from django.shortcuts import render
from rest_framework import viewsets
from .models import Artigo, Palavra
from .serializers import ArtigoSerializer, PalavraSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import spacy
from collections import Counter
from tika import parser
from encodings import utf_8
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.luhn import LuhnSummarizer
import nltk
from transformers import pipeline
import jsons
from django.shortcuts import  get_object_or_404
nltk.download('punkt')


@api_view(['GET'])
def member_api(request):
    nomePdf = "48500.006904-2019-52"
    parsed_pdf = parser.from_file(nomePdf+".pdf")
    """Palavras com mais frequencia"""
    data = parsed_pdf['content']
  

    """Processo"""
    novodata = data.split("\n")
    primeiraLetraProcesso = data.find("P")
    processo = data[primeiraLetraProcesso+10:primeiraLetraProcesso+30]

    """Interessado"""
    interessadoInicio = data.find("INTERESSAD")
    interessadoFinal = data.find("RELATOR")
    interesado = remover2pontos(data[interessadoInicio:interessadoFinal])


    """Relator"""
    relatorInicio = data.find("RELATOR")
    relatorFinal = data.find("RESPONSÁVEL:")
    relator = remover2pontos(data[relatorInicio:relatorFinal])
  

    """RESPONSÁVEL"""
    responsavelInicio = data.find("RESPONSÁVEL:")
    responsavelFinal = data.find("ASSUNTO:")
    responsavel = remover2pontos(data[responsavelInicio:responsavelFinal])

    """Assunto"""
    assuntoInicio = data.find("ASSUNTO:")
    assuntoFinal = data.find("I – RELATÓRIO")
    assunto= remover2pontos(data[assuntoInicio:assuntoFinal])
    
   
    """Dispositivo"""
    dispositivoInicio = data.find("– DISPOSITIVO")
    dispositivoFinal = data.find("Brasília,")
    dispositivo = data[dispositivoInicio+14:dispositivoFinal]

    artigo = ArtigoSerializer(
        data={
            "nome": nomePdf, 
            "processo":processo, 
            "dispositivo":dispositivo, 
            "assunto":assunto, 
            "responsavel":responsavel, 
            "relator": relator, 
            'interesado': interesado
        })
  

    if artigo.is_valid():
        palavrasChaves = palavrasComMaiorFrequencia(data)
        artigo.save()
        artigoId = Artigo.objects.get(nome=nomePdf)
        listaPalavrasChaves = ""
        for palavraChave in palavrasChaves: 
            listaPalavrasChaves = palavraChave[0]+','+ listaPalavrasChaves
            
        palavra = PalavraSerializer(data={"FKArtigoId": artigoId.id,"Palavra":listaPalavrasChaves})
        
        if palavra.is_valid():
            palavra.save()

    return Response("Salvo com sucesso")

@api_view(['GET'])
def lista_artigos_palavras(request):
    
    palavra = Palavra.objects.select_related('FKArtigoId')
    serializer = PalavraSerializer(palavra, many=True)
    return Response(serializer.data)
            

        
        

    
    """print(common_nouns)"""

    """Sumarizador - sumy
    parserDocument = PlaintextParser.from_string(data, Tokenizer('portuguese'))
    sumarizador = LuhnSummarizer()
    resumo = sumarizador(parserDocument.document, 5)
    for sentenca in resumo:
        print(sentenca)
    """

    """Sumarizador - transformrs
    transformrs=pipeline("summarization")
    t=transformrs(data)[0]['summary_text']
    """

    

def palavrasComMaiorFrequencia(data):
    nlp = spacy.load("pt_core_news_sm")
    nlp.Defaults.stop_words |= {'ccee', '\n\n', '\\n',"n", "nº"}
    doc = nlp(data)
    nouns = [
    token.text.lower() for token in doc if
        token.is_stop is False
        and token.is_punct is False
        and token.pos_ != "NUM"
        and token.pos_ != "PRON"
        and token.pos_ != "SYM"
        and len(token) > 3
    ]
    noun_freq = Counter(nouns)
    common_nouns = noun_freq.most_common(5)
    return common_nouns

def remover2pontos(data):
    dataInicio = data.rfind(":")
    return data[dataInicio+1:]

    

