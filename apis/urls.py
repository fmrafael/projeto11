from . import views
from django.urls import path


app_name = "apis"

urlpatterns = [
  path("apis/search_key", views.SearchKeyView.as_view(), name="search_key"),
  path("apis/whatsapp", views.WhatsappView.as_view(), name="whatsapp"),
    
]