from django.urls import path
from .views import SumaView, RestaView, MultiView, DivisionView

urlpatterns = [
    path ('sumar', SumaView.as_view()),
    path ('resta', RestaView.as_view()),
    path ('multi', MultiView.as_view()),
    path ('division', DivisionView.as_view())
]
