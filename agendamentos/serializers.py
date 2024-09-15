from rest_framework import serializers
from .models import agendamentopagamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = agendamentopagamento
        fields = '__all__'