from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'save_count', 'get_title']
    list_display_links = ['title', 'description', 'save_count', 'get_title']

    @admin.display(ordering='theme__title', description='Theme')
    def get_title(self, obj):
        if obj.theme is not None:
            return obj.theme.title
        else:
            return None


@admin.register(RequiredIngredient)
class RequiredIngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'substitute', 'get_title']
    list_display_links = ['name', 'quantity', 'substitute', 'get_title']

    @admin.display(ordering='recipe__title', description='Recipe')
    def get_title(self, obj):
        return obj.recipe.title


@admin.register(AdditionalIngredient)
class AdditionalIngredientsAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'substitute', 'get_title']
    list_display_links = ['name', 'quantity', 'substitute', 'get_title']

    @admin.display(ordering='recipe__title', description='Recipe')
    def get_title(self, obj):
        return obj.recipe.title


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_title']
    list_display_links = ['name', 'get_title']

    @admin.display(ordering='recipe__title', description='Recipe')
    def get_title(self, obj):
        return obj.recipe.title


@admin.register(RecipeSequence)
class RecipeSequenceAdmin(admin.ModelAdmin):
    list_display = ['order', 'short_desc', 'get_title']
    list_display_links = ['order', 'short_desc', 'get_title']

    @admin.display(ordering='recipe__title', description='Recipe')
    def get_title(self, obj):
        return obj.recipe.title
