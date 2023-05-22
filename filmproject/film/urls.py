from django.urls import path
from film import views

urlpatterns = [
    path('detail/<int:id>/', views.detail, name = "detail"),
    path('delete_comment/<int:id>/', views.delete_comment, name = "delete_comment"),
    path('category/<int:id>/', views.category, name = "category")
]