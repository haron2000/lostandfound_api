from django.shortcuts import render
from rest_framework import viewsets, filters, generics, permissions
from .models import LostFoundID
from .serializers import LostFoundIDSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import generics, permissions
from .models import LostFoundID
from .serializers import LostFoundIDSerializer

# List all and allow new reports
class LostFoundIDListCreateView(generics.CreateAPIView):
    serializer_class = LostFoundIDSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Search by ID number
class LostFoundIDSearchView(generics.ListAPIView):
    serializer_class = LostFoundIDSerializer

    def get_queryset(self):
        id_number = self.request.query_params.get('id_number', '').strip()
        if id_number:
            return LostFoundID.objects.filter(id_number__iexact=id_number)
        # Return empty queryset if id_number not provided
        return LostFoundID.objects.none()


        
    

def submit_view(request):
    return render(request, 'submit.html')

def search_view(request):
    return render(request, 'search.html')




