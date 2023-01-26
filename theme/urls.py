from django.urls import path

from theme.views import ThemeListView, ThemeDetailView, ThemeSearchView

urlpatterns = [
    path('', ThemeListView.as_view(), name="theme_list"),
    path('<int:id>', ThemeDetailView.as_view(), name="theme_detail"),
    path('search/', ThemeSearchView.as_view(), name="theme_search")
]