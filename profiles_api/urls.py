from . import views
from django.urls import path

urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view())
]