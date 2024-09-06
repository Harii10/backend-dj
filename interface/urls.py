from django.urls import path
from .views import material_list, bmaterials_list, nested_list, index

urlpatterns = [
    path('', index),
    path('list/', material_list),
    path('chartlist/', bmaterials_list),
    path('nestedlist/', nested_list)

]