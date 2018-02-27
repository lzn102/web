from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path(r"", views.index, name="index"),
    path(r"detail/<int:title_id>/", views.detail, name="detail"),
    path(r"write/", views.write, name="write"),
]