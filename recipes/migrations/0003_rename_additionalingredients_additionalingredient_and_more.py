# Generated by Django 4.1.4 on 2022-12-30 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_theme'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdditionalIngredients',
            new_name='AdditionalIngredient',
        ),
        migrations.RenameModel(
            old_name='RequiredIngredients',
            new_name='RequiredIngredient',
        ),
    ]
