from django.urls import path
from .views import *

app_name = 'recipes'

urlpatterns = [
    path('list/', RecipeListView.as_view()),
    path('list_in_theme/<int:pk>/', RecipeListInThemeView.as_view()),
    path('<int:pk>/', RecipeDetailView.as_view()),
    path('search/', RecipeSearchView.as_view()),
]
