from django.urls import path, include
from . import views
from .views import LibraryDetailView

urlpatterns = [
    # Function-based view URL
    path('books/', views.list_books, name='list_books'),
    # Class-based view URL
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]