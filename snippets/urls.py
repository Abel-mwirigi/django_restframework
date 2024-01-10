from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetsDetailView.as_view()),
    path('list/', views.SnippetsListView.as_view())
]