from django.shortcuts import render
from rest_framework import viewsets
from .models import Artigo
from .serializers import ArtigoSerializer
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
nltk.download('punkt')
# Create your views here.
# api_view

@api_view(['GET'])
def member_api(request):
    nlp = spacy.load("pt_core_news_sm")
    nlp.Defaults.stop_words |= {'ccee', '\n\n', '\\n',"n", "nº"}
    parsed_pdf = parser.from_file("48500.006904-2019-52.pdf")
    """Palavras com mais frequencia"""
    data = parsed_pdf['content']
    doc = nlp(data)
    nouns = [
    token.text.lower() for token in doc if
        token.is_stop is False
        and token.is_punct is False
        and token.pos_ != "NUM"
        and token.pos_ != "PRON"
        and token.pos_ != "SYM"
    ]
    noun_freq = Counter(nouns)
    common_nouns = noun_freq.most_common(5)
    print(common_nouns)

    """Sumarizador"""
    parserDocument = PlaintextParser.from_string(data, Tokenizer('portuguese'))
    sumarizador = LuhnSummarizer()
    resumo = sumarizador(parserDocument.document, 5)
    for sentenca in resumo:
        print(sentenca)
  
    return Response(common_nouns)

   
