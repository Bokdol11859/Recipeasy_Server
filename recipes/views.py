from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *


# Create your views here.


class RecipeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({'message': '레시피 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)


class RecipeListInThemeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        recipes = Recipe.objects.filter(theme=pk)
        serializer = RecipeSerializer(recipes, many=True)
        return Response({'message': '테마에 속하는 레시피 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)


class RecipeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer = RecipeDetailSerializer(recipe)
        return Response({'message': '레시피 상세 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)


class RecipeSearchView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RecipeSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = Recipe.objects.filter(
            Q(title__icontains=query) | Q(
                required_ingredients__name__icontains=query)
        ).distinct()
        return queryset_list
