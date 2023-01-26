from rest_framework import serializers

from recipes.serializers import RecipeSerializer
from theme.serializers import ThemeSerializer
from user.models import User


class UserSerializer(serializers.ModelSerializer):

    saved_themes = ThemeSerializer(many=True, required=False)
    saved_recipes = RecipeSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ['nickname', 'saved_themes', 'saved_recipes']
