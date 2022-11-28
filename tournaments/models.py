from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Tournament(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateTimeField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=64)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="groups")
    teams = models.ManyToManyField(Team, related_name="+")

    def __str__(self):
        return self.name


class Game(models.Model):
    NOT_STARTED = 0
    ONGOING = 1
    FINISHED = 2
    STATUS = (
        (NOT_STARTED, "Not started"),
        (ONGOING, "Ongoing"),
        (FINISHED, "Finished")
    )

    GROUP = 1
    PLAYOFF = 2
    TYPE = (
        (GROUP, "Group game"),
        (PLAYOFF, "Playoff")
    )

    home = models.ManyToManyField(Team, related_name="home_games")
    away = models.ManyToManyField(Team, related_name="away_games")
    home_score = models.IntegerField(blank=True, null=True)
    away_score = models.IntegerField(blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        choices=STATUS,
        default=NOT_STARTED
    )
    tournament = models.ForeignKey(Tournament, on_delete=models.SET_NULL, null=True, related_name="games")

    @property
    def winner(self):
        if self.status == self.FINISHED:
            if self.home_score > self.away_score:
                return self.home
            elif self.home_score < self.away_score:
                return self.away
            else:
                return "tie"

    def __str__(self):
        return f"{self.home} - {self.away}: {self.status}"
