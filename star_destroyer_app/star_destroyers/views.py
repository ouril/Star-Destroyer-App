from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import StarDestroyer
from .serializer import StarDestroyerSerializer


class StarDesroyersViewSet(viewsets.ModelViewSet):
    queryset = StarDestroyer.objects.all()
    serializer_class = StarDestroyerSerializer
    permission_classes = [AllowAny]