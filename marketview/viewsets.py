from rest_framework import viewsets
from .models import Symbol
from .serializers import SymbolSerializer

class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.
    serializer_class = ArticleSerializer