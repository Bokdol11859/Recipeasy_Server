from rest_framework import serializers

from recipes.serializers import RecipeSerializer
from theme.models import Theme, ThemeType


class ThemeSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = Theme
        fields = ["id", "title", "description", "recipe_count", "save_count", "duration", "tips", "theme_type", "recipes", 'landscape_image', 'portrait_image']


class ThemeTypeSerializer(serializers.ModelSerializer):
    themes = ThemeSerializer(many=True)

    class Meta:
        model = ThemeType
        fields = ["id", "title", "themes"]




