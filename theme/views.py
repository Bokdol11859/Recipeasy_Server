from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer
from theme.models import Theme, ThemeType
from theme.serializers import ThemeSerializer, ThemeTypeSerializer
from user.models import User


class ThemeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        theme_types = ThemeType.objects.all()
        theme_types_serializer = ThemeTypeSerializer(theme_types, many=True)
        theme_list = Theme.objects.all()
        theme_list_serializer = ThemeSerializer(theme_list, many=True)
        return Response({"Theme Types": theme_types_serializer.data, "Themes": theme_list_serializer.data},
                        status=status.HTTP_200_OK)


class ThemeDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        theme = get_object_or_404(Theme, id=id)
        print(theme.theme_type.title)
        serializer = ThemeSerializer(theme)
        return Response({"theme": serializer.data, 'theme_type_name': theme.theme_type.title}, status=status.HTTP_200_OK)


    def post(self, request, id):
        theme = get_object_or_404(Theme, id=id)
        user = User.objects.get(username=request.user.username)
        if user in theme.saved_user.all():
            theme.saved_user.remove(user)
            theme.save_count -= 1
            theme.save()
            return Response({"Message": "Theme unsaved successfully"}, status=status.HTTP_200_OK)
        else:
            theme.saved_user.add(user)
            theme.save_count += 1
            theme.save()
            return Response({"Message": "Theme saved successfully"}, status=status.HTTP_200_OK)



class ThemeSearchView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ThemeSerializer

    def get_queryset(self, *args, **kwargs):
        query = self.request.GET.get("q")
        queryset_list = Theme.objects.filter(
            Q(title__icontains=query) | Q(
                description__icontains=query)
        ).distinct()
        return queryset_list
