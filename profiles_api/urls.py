from . import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
"""Registering a specific viewset with our router"""
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')

urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]