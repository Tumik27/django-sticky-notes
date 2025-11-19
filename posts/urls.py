from django.urls import path
from .views import post_list, post_detail   # ← changed this line

urlpatterns = [
    path('', post_list, name='post_list'),           # root = list
    path('post/<int:pk>/', post_detail, name='post_detail'),  # detail with pk
]