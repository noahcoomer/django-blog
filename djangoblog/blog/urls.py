from django.urls import path
from . import views

urlpatterns = [
    # index page
    path('', views.index, name='blog_index'),
    # view posts <int:year>/<int:month>/<int:day>/
    path('view/<int:year>/<int:month>/<int:day>/<slug:slug>.html', views.view_post, name='view_post'),
    # view categories
    path('category/<slug:slug>.html', views.view_category, name='view_category'),
    # view archives
    path('view/<int:year>/<int:month>/', views.view_archive, name='view_archive'),
]
