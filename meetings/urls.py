from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.detail, name='detail'),
    path('rooms/<int:id>', views.roomDetail, name='roomDetail'),
    path('new', views.new, name='new'),
]
