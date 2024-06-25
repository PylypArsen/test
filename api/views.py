from django.shortcuts import render
from rest_framework import generics
from .models import Team, Human
from .serializers import TeamSerializer, HumanSerializer

# I wrote the view this way because, in commercial products, 
#   they are usually customized and rewritten. This approach is the best way 
#   to create a reusable view for that small app.

class TeamAPIList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamAPICreate(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamAPIRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class HumanAPIList(generics.ListAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

class HumanAPICreate(generics.CreateAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer

class HumanAPIRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer