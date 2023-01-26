from rest_framework import serializers
from .models import *


class RequiredIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredIngredient
        fields = ['name', 'quantity', 'substitute', 'emoji']


class RequiredIngredientSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredIngredient
        fields = ['name']


class AdditionalIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalIngredient
        fields = ['name', 'quantity', 'substitute', 'emoji']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name']


class RecipeSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeSequence
        fields = ['order', 'short_desc', 'long_desc', 'image']


class RecipeSerializer(serializers.ModelSerializer):
    required_ingredients = RequiredIngredientSimpleSerializer(
        many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'video_id', 'title', 'time_taken',
                  'save_count', 'required_ingredients', 'theme', 'image']


class RecipeDetailSerializer(serializers.ModelSerializer):
    required_ingredients = RequiredIngredientSerializer(
        many=True, read_only=True)
    additional_ingredients = AdditionalIngredientSerializer(
        many=True, read_only=True)
    equipment = EquipmentSerializer(many=True, read_only=True)
    recipe_sequence = RecipeSequenceSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'description', 'difficulty', 'time_taken', 'save_count',
                  'required_ingredients', 'additional_ingredients', 'equipment', 'recipe_sequence', 'video_id']
