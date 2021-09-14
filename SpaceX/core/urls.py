from django.urls import path
from .views import CardCreation
urlpatterns = [
    path('card_create/',CardCreation.as_view(),name ="create")
]

