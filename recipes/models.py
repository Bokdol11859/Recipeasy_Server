from django.db import models
from theme.models import Theme
# Create your models here.
from user.models import User


class Recipe(models.Model):
    video_id = models.CharField(max_length=2000)
    image = models.URLField(max_length=2000)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    difficulty = models.IntegerField(default=3)
    time_taken = models.CharField(max_length=20)
    save_count = models.IntegerField(default=0)
    saved_user = models.ManyToManyField(
        User, related_name='saved_recipes', blank=True, null=True)
    theme = models.ForeignKey(
        Theme, blank=True, null=True, on_delete=models.SET_NULL, related_name='recipes')

    def __str__(self):
        return f'{self.title}'


class RequiredIngredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=30)
    substitute = models.CharField(max_length=50, blank=True, null=True)
    emoji = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, related_name='required_ingredients')

    def __str__(self):
        return f'{self.name}'


class AdditionalIngredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.CharField(max_length=30)
    substitute = models.CharField(max_length=50, blank=True, null=True)
    emoji = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, related_name='additional_ingredients')

    def __str__(self):
        return f'{self.name}'


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, related_name='equipment')

    def __str__(self):
        return f'{self.name}'


class RecipeSequence(models.Model):
    order = models.IntegerField()
    short_desc = models.CharField(max_length=300)
    long_desc = models.CharField(max_length=1000)
    image = models.URLField(max_length=2000)
    recipe = models.ForeignKey(
        'Recipe', on_delete=models.CASCADE, related_name='recipe_sequence')

    def __str__(self):
        return f'({self.order}) {self.short_desc[:10]}'
