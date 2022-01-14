from django.shortcuts import render
from rest_framework import generics

from write.models import Write
from .models import Write
from .serializers import WriteSerializer
from .permissions import IsAuthorOrReadOnly
class WriteList(generics.ListCreateAPIView):
    queryset = Write.objects.all()
    serializer_class = WriteSerializer

class WriteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Write.objects.all()
    serializer_class = WriteSerializer    