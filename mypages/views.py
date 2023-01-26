from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from recipes.serializers import *
from recipes.models import *


class RecipeSaveView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        user = request.user
        is_bookmarked = False
        if recipe in user.saved_recipes.all():
            user.saved_recipes.remove(recipe)
            recipe.save_count -= 1
        else:
            user.saved_recipes.add(recipe)
            recipe.save_count += 1
            is_bookmarked = True

        serializer = RecipeSaveSerializer(
            data=request.data, instance=recipe, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '레시피 저장 토글 성공', 'data': {'id': serializer.data['id'], 'title': serializer.data['title'], 'save_count': serializer.data['save_count'], 'is_saved': is_bookmarked}}, status=HTTP_200_OK)
        return Response({'message': '레시피 저장 토글 실패', 'data': serializer.data}, status=HTTP_400_BAD_REQUEST)


class RecipeSaveListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        recipes = request.user.saved_recipes.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({'message': '저장한 레시피 목록 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)
