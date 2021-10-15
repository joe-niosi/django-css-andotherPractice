from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('show/<int:user_id>', views.show),
    path('<int:blog_num>/edit', views.edit),
    path('<int:blog_num>/delete',views.destroy),
]