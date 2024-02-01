from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lista'),
    path('view/<int:id>', views.view, name="lista_view"),
    path('edit/<int:id>', views.edit, name="lista_edit"),
    path('create/', views.create, name="lista_create"),
    path('delete/<int:id>', views.delete, name="lista_delete"),
]

