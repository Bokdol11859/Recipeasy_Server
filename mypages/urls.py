from django.urls import path
from .views import *

app_name = 'mypages'

urlpatterns = [
    path('recipes/<int:pk>/', RecipeSaveView.as_view()),
    path('recipes/', RecipeSaveListView.as_view()),
]
