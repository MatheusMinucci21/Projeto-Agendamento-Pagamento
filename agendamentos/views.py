from rest_framework import generics
from .models import agendamentopagamento
from .serializers import AgendamentoSerializer

#############Classes para auxiliar criar, listar, visualizar e deletar informações atraves da API########

#API Para criação de de um input de informação
class AgendamentoCreate(generics.CreateAPIView):
    queryset = agendamentopagamento.objects.all()
    serializer_class = AgendamentoSerializer

#API Para Listar  de de um input de informação
class AgendamentoList(generics.ListAPIView):
    queryset = agendamentopagamento.objects.all()
    serializer_class = AgendamentoSerializer

#API Para Detalhar de de um input de informação
class AgendamentoDetail(generics.RetrieveAPIView):
    queryset = agendamentopagamento.objects.all()
    serializer_class = AgendamentoSerializer

#API Para Deletar de de um input de informação
class AgendamentoDelete(generics.DestroyAPIView):
    queryset = agendamentopagamento.objects.all()
    serializer_class = AgendamentoSerializer

