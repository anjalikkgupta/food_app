from django.urls import path
from .views import IngredientList,IngredientDetail
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	# path('inglist/', views.ingredients_list, name='ingredients_list')
	path('test/', views.ing_list, name='ing_list'),
	path('test_dhruv/', views.get_food_fe, name='inge'),
	path('new/', views.food_new, name='food_new'),

	path('ing/', IngredientList.as_view(), name="ingredient_list"),
	path('ing/<int:pk>', IngredientDetail.as_view(), name="ingredient_detail"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

