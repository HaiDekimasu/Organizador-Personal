from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='contactos'),
    path('view/<int:id>', views.view, name="contactos_view"),
    path('edit/<int:id>', views.edit, name="contactos_edit"),
    path('create/', views.create, name="contactos_create"),
    path('delete/<int:id>', views.delete, name="contactos_delete"),
]
