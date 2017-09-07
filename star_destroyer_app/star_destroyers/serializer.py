from rest_framework.serializers import ModelSerializer

from .models import StarDestroyer


class StarDestroyerSerializer(ModelSerializer):
    class Meta:
        model = StarDestroyer
        fields = '__all__'

