from django.urls import path, include

from .views import submit_view, search_view, LostFoundIDListCreateView, LostFoundIDSearchView



urlpatterns = [
    
    path('ids/', LostFoundIDListCreateView.as_view(), name='list_create_ids'),
    path('ids/search/', LostFoundIDSearchView.as_view(), name='search_ids'),
    path('submit/', submit_view),
    path('search/', search_view),
]
