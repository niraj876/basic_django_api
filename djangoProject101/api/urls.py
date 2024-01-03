from django.urls import path
from .views import DemoApi

urlpatterns = [
    path("apicall", DemoApi.as_view()),
]