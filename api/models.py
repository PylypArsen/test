from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name

class Human(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    mail = models.EmailField(max_length=254)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name