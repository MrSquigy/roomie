# Copyright (c) 2021 Jonathan Vice

from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
