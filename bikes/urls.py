from django.urls import path
from . import views

urlpatterns = [
    path('', views.bike_list, name='bike_list'),
    path('rent/<int:bike_id>/', views.rent_bike, name='rent_bike'),
    path('add/',views.add_bike,name='add_bike'),
    path('delete/<int:bike_id>/',views.delete_bike,name='delete_bike'),
]
