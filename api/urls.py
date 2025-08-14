from django.urls import path
from .views import *
from .views import visualizacao_autor

urlpatterns = [
    path('autores', AutoresView.as_view()),
    path('authors', visualizacao_autor)
]
