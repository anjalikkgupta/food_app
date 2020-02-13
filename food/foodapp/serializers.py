from rest_framework import serializers
from .models import Food, Ingredients

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = ["nutrients","value","unit"]


class FoodSerializer(serializers.ModelSerializer):
	ingredients = IngredientSerializer(many=True, read_only=True)

	class Meta:
		model = Food
		fields = ["food_name", "added_date", "ingredients"]
        

