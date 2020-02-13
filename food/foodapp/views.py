from django.shortcuts import render,redirect
# from .models import Ingredients, Food
# # Create your views here.
# def ingredients_list(request):
# 	# ingrdients = Ingredients.objects.filter(food=1)
# 	food = Food.objects.filter(food_name='Biryani').first()
# 	# print(doo.food_name)
# 	# print(ingrdients.added_date)
# 	ingre = food.ingredients.all()
# 		# print(a)
	

# 	return render(request, 'ingredients_list.html', {'ingrdients':ingre,'food':food})


from .models import Ingredients,Food
from .serializers import FoodSerializer, IngredientSerializer
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import filters
from .forms import FoodForm
from django.generics.edit import CreateView, UpdateView
from django.generics.list import ListView
# class IngredientList(generics.ListCreateAPIView):
# 	Model = Ingredients
# 	serializer_class = IngredientSerializer
	
# 	def get_queryset(self):
# 		queryset = Ingredients.objects.all()
# 		print(queryset)
# 		food = self.request.query_params.get('food')
# 		print(food)
		
# 		if food:
# 			queryset = queryset.filter(food_id=food)
# 		return queryset
	
	
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = FoodSerializer
	queryset = Food.objects.all()
	#template_name = 'ingredients_list.html'
	
class IngredientList(generics.ListCreateAPIView):
	search_fields = ['=food_name']
	filter_backends = (filters.SearchFilter,)
	serializer_class = FoodSerializer
	queryset = Food.objects.all()



def ing_list(request):
	foods = Food.objects.all()
	return render(request, 'foodapp/test.html', {'foods': foods})

def get_food_fe(request):
	return render(request, 'foodapp/base.html')


def food_new(request):
	if request.method == 'POST':
		form = FoodForm(request.POST)
		if form.is_valid():
			food = form.save(commit=False)
			food.save()
			return redirect('ingredient_detail', pk=food.pk)
	else:

		form = FoodForm()
	return render(request, 'foodapp/test_form.html', {'form':form})


class FoodCreateView(CreateView):
	Model = Food
	fields = ['food_name','added_date','nutrients','value','unit',]
	def get_context_data(self, **kwargs):
		# we need to overwrite get_context_data
		# to make sure that our formset is rendered
		data = super().get_context_data(**kwargs)
		if self.request.POST:
			data["ingrdientss"] = FoodForm(self.request.POST)
		else:
			data["ingrdientss"] = FoodForm()
		return data

	def form_valid(self, form):
		context = self.get_context_data()
		ingrdientss = context["ingrdientss"]
		self.object = form.save()
		if ingrdientss.is_valid():
			ingrdientss.instance = self.object
			ingrdientss.save()
		return super().form_valid(form)
