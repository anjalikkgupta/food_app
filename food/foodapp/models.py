from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.
class Food(models.Model):
	food_name = models.CharField(max_length=200)
	added_date = models.DateTimeField(default=timezone.now)
	# ingredients = GenericRelation(Ingredients)
 
	def __str__(self):
		return self.food_name

class Ingredients(models.Model):
	food =models.ForeignKey(Food, on_delete=models.CASCADE, related_name='ingredientss')
	nutrients = models.CharField(max_length=200)
	value = models.IntegerField(default=0)
	unit = models.CharField(max_length=10)

	def __str__(self):
		return self.nutrients

	