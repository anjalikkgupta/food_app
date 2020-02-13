from django import forms
from .models import Food,Ingredients
from django.forms.models import inlineformset_factory

FoodForm = inlineformset_factory(Food,Ingredients, fields=('food_name','added_date','nutrients','value','unit',))

# class FoodForm(forms.ModelForm):

# 	ingredient = forms.ModelChoiceField(queryset=Ingredients.objects.all())

# 	class Meta:
# 		model = Food
# 		fields = ('food_name','added_date','ingredient')
# 	