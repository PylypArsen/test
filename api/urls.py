from api.views import *
from django.urls import path

urlpatterns = [
    path("teams/", TeamAPIList.as_view()),
    path("teams/create", TeamAPICreate.as_view()),
    path("teams/<int:pk>", TeamAPIRetrieveUpdateDelete.as_view()),
    path("humans/", HumanAPIList.as_view()),
    path("humans/create", HumanAPICreate.as_view()),
    path("humans/<int:pk>", HumanAPIRetrieveUpdateDelete.as_view())
    
]