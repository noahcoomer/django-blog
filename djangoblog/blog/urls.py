from django.urls import path
from . import views

urlpatterns = [
    # index page
    path('', views.index, name='blog_index'),
    # view posts
    path('view/<slug:slug>.html', views.view_post, name='view_post'),
    # view categories
    path('category/<slug:slug>.html', views.view_category, name='view_category'),
]
