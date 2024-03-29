from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer

class SnippetsDetailView(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetsListView(generics.ListAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer