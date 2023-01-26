from rest_framework import serializers
from recipes.models import Recipe


class RecipeSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'save_count']
