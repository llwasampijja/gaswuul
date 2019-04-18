from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from redflag.models import Redflag
from redflag.serializers import RedflagSerializer


class RedflagViewSet(ModelViewSet):
    queryset = Redflag.objects.all().order_by('date')
    serializer_class = RedflagSerializer

    def perform_create(self, serializer):
        """API endpoint for creating a redflag"""
        serializer.save(createdby=self.request.user)
