from saved_messages import views
from django.urls import path

# The API URLs are now determined automatically by the router.
urlpatterns = [
  path('', views.MessageList.as_view()),
  path('create/', views.MessageCreate.as_view()),
  path('delete/<int:pk>/', views.MessageDelete.as_view()),
]