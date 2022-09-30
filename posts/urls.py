from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,AboutPage


urlpatterns = [
    path('', PostListView.as_view(), name='list'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('new/',PostCreateView.as_view(), name='new'),
    path('about/', AboutPage.as_view(), name='about'),
    ]