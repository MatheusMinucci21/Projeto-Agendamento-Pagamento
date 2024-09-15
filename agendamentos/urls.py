from django.urls import path
from .views import AgendamentoCreate, AgendamentoList, AgendamentoDetail, AgendamentoDelete


#import das views para criar e gerencias as URLS no postman (agendamentos)
urlpatterns = [
    #URL para fazer o Upload Criar

    path('agendamentos/create/', AgendamentoCreate.as_view(), name='create_agendamento'),

    # URL para o GET para Visualizar toda a lista
    path('agendamentos/', AgendamentoList.as_view(), name='list_agendamentos'),

    # URL para GET de determinado ID no banco de dados EX: agendamentos/1/
    path('agendamentos/<int:pk>/', AgendamentoDetail.as_view(), name='detail_agendamento'),

    #URL para Deletar determinado ID no banco de dados EX : agendamentos/1/
    path('agendamentos/delete/<int:pk>/', AgendamentoDelete.as_view(), name='delete_agendamento'),
]