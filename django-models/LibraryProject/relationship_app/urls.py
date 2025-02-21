from django.urls import path
from . import views
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView
from .views import list_books

urlpatterns = [
    # Function-based view URL
    path('books/', views.list_books, name='list_books'),
    # Class-based view URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('', views.home_view, name='home'),  # Example home page
]