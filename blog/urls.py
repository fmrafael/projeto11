from . import views
from django.urls import path


app_name = "blog"

urlpatterns = [
  path("blog/", views.PostListView.as_view(), name=""),
  path("<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
  #path('blog/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
   
  
] 