from rest_framework import viewsets
from rest_framework import permissions
from .models import Tournament, Group, Game, Team
from .serializers import TournamentSerializer, GroupSerializer, TeamSerializer, GameSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tournaments to be viewed or edited.
    """
    queryset = Tournament.objects.all().order_by('-date')
    serializer_class = TournamentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    # permission_classes = [permissions.IsAuthenticated]
