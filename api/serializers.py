from rest_framework import serializers
from .models import Team, Human

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = "__all__"