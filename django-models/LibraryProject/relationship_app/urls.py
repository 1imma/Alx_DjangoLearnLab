from django.urls import path
from . import views
from .views import LibraryDetailView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView
from .views import list_books, register_view

urlpatterns = [
    # Function-based view URL
    path('books/', views.list_books, name='list_books'),
    # Class-based view URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('', views.home_view, name='home'),  # Example home page
    path('admin-dashboard/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]